import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials as sac
import xml.etree.ElementTree as ET

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


DATABASE = "kanalservis"
USER = "postgres"
PASSWORD = "postgres"
HOST = "localhost"
PORT = "5432"


def getting_data_from_sheets(spreadsheet_name, sheet_num):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']  # это уровень доступа, который хочет наше приложение от Google API
    credentials_path = 'kanalservis-351307-dbb5748332b1.json'  # название файла с учетными данными

    # Мы извлекаем учетные данные по указанному пути и используем их для авторизации доступа к электронным таблицам
    # Google через Python.
    credentials = sac.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(credentials)

    # авторизованный клиент используется для открытия электронной таблицы, выбора определенного листа и
    # извлечения всех записей в виде словаря. В конце концов словарь преобразуется в DataFrame.
    sheet = client.open(spreadsheet_name).get_worksheet(sheet_num).get_all_records()
    print('Данные из Google Sheets успешно получены')

    return sheet  # type: list


def add_new_column(data) -> list:
    res = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp').text  # type: str
    root = ET.fromstring(res)
    dollar_to_ruble = float(root[11][4].text.replace(',', '.'))  # type: float

    for row in data:
        row['стоимость в руб.'] = (row['стоимость,$'] * dollar_to_ruble).__round__()

    print('Новая колонка успешно добавлена')

    return data  # type: list


def update_db(dataframe):

    connection_string = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

    if not database_exists(connection_string):
        create_database(connection_string)

    engine = create_engine(connection_string)
    connection = engine.connect()

    dataframe.to_sql('kanalservis', con=engine, if_exists='replace', index=False)
    connection.execute('select * from kanalservis')

    print('Данные в БД обновлены')
