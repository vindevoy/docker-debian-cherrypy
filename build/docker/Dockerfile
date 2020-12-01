FROM vindevoy/debian10-base:latest

ARG CHERRYPY_VERSION="18.6.0"

LABEL maintainer="Yves Vindevogel (vindevoy) - yves.vindevogel@asynchrone.com"

RUN set -x && \ 
    apt-get update -y && \ 
    apt-get upgrade -y && \ 
    apt-get install python3.7 -y && \ 
    apt-get install python3-pip -y && \ 
    pip3 install cherrypy==$CHERRYPY_VERSION && \ 
    apt-get autoremove && \ 
    apt-get clean all && \ 
    mkdir -p /opt/cherrypy

COPY resources/main.py /opt/cherrypy/main.py

EXPOSE 8080

WORKDIR /opt/cherrypy

CMD ["python3", "/opt/cherrypy/main.py"]
