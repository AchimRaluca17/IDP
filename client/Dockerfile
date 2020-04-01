FROM python:3.6

RUN apt update && \
    apt install -y netcat-openbsd

# Place app in container.
COPY . /opt/client
WORKDIR /opt/client

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["/bin/bash", "entrypoint.sh"]