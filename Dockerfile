FROM python:3.7.1-stretch

ENV ROOT_PATH /project/app

RUN mkdir -p $ROOT_PATH

ADD requirements.txt $ROOT_PATH
WORKDIR $ROOT_PATH

RUN pip install -r requirements.txt

ADD . $ROOT_PATH

EXPOSE 5000

CMD gunicorn app:app -b 0.0.0.0:5000 -w 2