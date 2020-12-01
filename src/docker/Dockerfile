###
#
#	Yves Vindevogel (vindevoy)
#	2020-11-30
#
#	Basic CentOS 8 image with Python and CherryPy installed on it
#
###
 
FROM vindevoy/debian10-base:latest

ARG CHERRYPY_VERSION="18.6.0"

LABEL maintainer="Yves Vindevogel (vindevoy) - yves.vindevogel@asynchrone.com"

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install python3.7 -y
RUN apt-get install python3-pip -y

RUN pip3 install cherrypy==$CHERRYPY_VERSION

RUN apt-get autoremove
RUN apt-get clean all

RUN mkdir -p /opt/cherrypy

COPY resources/main.py /opt/cherrypy/main.py

EXPOSE 8080

WORKDIR /opt/cherrypy
CMD ["python3", "/opt/cherrypy/main.py"]
