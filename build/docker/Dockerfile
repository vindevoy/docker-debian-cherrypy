FROM debian:10.11-slim

ARG CHERRYPY_VERSION="18.6.1"

LABEL maintainer="Yves Vindevogel (vindevoy) - yves.vindevogel@asynchrone.com"

RUN set -x && \ 
    apt-get update -y && \ 
    apt-get dist-upgrade -y && \ 
    apt-get install python3.7 --no-install-recommends -y && \ 
    apt-get install python3-pip --no-install-recommends -y && \ 
    pip3 install cherrypy==$CHERRYPY_VERSION && \ 
    apt-get autoremove && \ 
    apt-get clean all && \ 
    mkdir -p /opt/cherrypy

COPY resources/main.py /opt/cherrypy/main.py

EXPOSE 8080

WORKDIR /opt/cherrypy

CMD ["python3", "/opt/cherrypy/main.py"]
