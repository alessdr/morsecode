FROM python:3.8.0

WORKDIR /usr/app

COPY .. .

RUN pip3 install -r requirements.txt

CMD gunicorn -w 1 -b 0.0.0.0:$PORT --threads 100 app:app
