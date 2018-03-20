FROM python:3.5-alpine

MAINTAINER Mikalai Charopkin (ncherepkin@live.com)

WORKDIR /opt

ADD . /opt

ENV FLASK_APP=server.py

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
