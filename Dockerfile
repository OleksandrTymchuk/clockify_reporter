FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /clockify_reporter
WORKDIR /clockify_reporter
ADD . /clockify_reporter/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient
COPY . /clockify_reporter/