FROM python:2.7.10

COPY start.sh /
COPY requirements.txt /

RUN chmod +x ./start.sh

RUN pip install -r requirements.txt

ENTRYPOINT ./start.sh
