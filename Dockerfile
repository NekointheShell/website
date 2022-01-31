FROM debian


ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN apt install -y nginx gunicorn python3 python3-pip


ADD . /website
RUN cd /website; pip install .; cp nginx.conf /etc/nginx/nginx.conf


CMD /website/daemon
