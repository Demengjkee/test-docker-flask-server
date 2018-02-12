FROM python:3.5-alpine

WORKDIR /opt

ADD . /opt

ENV FLASK_APP=server.py

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]