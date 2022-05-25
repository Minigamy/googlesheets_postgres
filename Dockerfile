FROM python:3

WORKDIR /opt/app

COPY ./req.txt /opt/app/requirements.txt

RUN pip install -r /opt/app/requirements.txt

COPY ./ /opt/app

CMD [ "python", "./scheduler.py" ]