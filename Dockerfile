FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /hacksarena
WORKDIR /hacksarena
COPY . /hacksarena/
RUN pip install -r requirements.txt
