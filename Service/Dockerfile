FROM python:3.6

MAINTAINER Raluca <raluca.achim@gmail.com>

RUN apt update && \
    apt install -y netcat-openbsd

COPY . /opt/service
WORKDIR /opt/service


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["/bin/bash", "entrypoint.sh"]