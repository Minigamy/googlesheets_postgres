from time import sleep

import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from main import getting_data_from_sheets, add_new_column, update_db


def foo():
    data = getting_data_from_sheets('kanalservis_table', 0)
    full_data = add_new_column(data)
    full_data = pd.DataFrame.from_dict(full_data)
    update_db(full_data)


def main():
    scheduler = BackgroundScheduler()
    scheduler.start()

    trigger = CronTrigger(
        year="*", month="*", day="*", hour="*", minute="*", second=59
    )
    scheduler.add_job(
        foo,
        trigger=trigger,
        name="daily foo",
    )
    while True:
        sleep(5)


if __name__ == "__main__":
    main()
