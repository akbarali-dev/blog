FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY . .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

EXPOSE 8000

COPY entrypoint.sh .
ENTRYPOINT ["sh", "entrypoint.sh"]













#FROM python:3.10
#
#ENV PYTHONDONTWRITEBYTECODE=1
#
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /code
#
#COPY requirements.txt /code/
#
#RUN pip install -r requirements.txt
#
#EXPOSE 8000
#
#COPY . /code/
#ENTRYPOINT ["./entrypoint.sh"]