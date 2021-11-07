FROM python:3.8.0

WORKDIR /usr/app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "--threads", "100", "app:app" ]
