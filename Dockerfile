FROM python:3.6

COPY requirements.txt requirements.txt

RUN pip install -U pip wheel setuptools \
 && pip install -r requirements.txt

ADD . .

EXPOSE 5000

CMD python web.py