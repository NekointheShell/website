FROM debian


ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN apt install -y nginx gunicorn rsyslog


ADD . /website
RUN cd /website; pip install .
