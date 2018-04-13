FROM python:3.6
LABEL maintainer="yun_tofar@qq.com"
LABEL version="1.0"
LABEL description="python flask scaffold"

COPY ./src /app

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt