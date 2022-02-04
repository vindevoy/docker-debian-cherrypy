###
#
#	Yves Vindevogel (vindevoy)
#	2022-02-04
#
#	Version 18.6.1
#
#   Features:
#       - Upgraded CherryPy version
#       - Upgraded Debian version
#
###
 
FROM debian:10.11-slim
# Debian 10 based because of Python version (upgraded to 3.9 in Debian 11, but CherryPy supports only up to Python 3.8)
# Note to myself: I removed the old 1.x tags because I'm now linking the Debian version to the image
#                 Once CherryPy is compatible with Python 3.9, the FROM should become my own image

ARG CHERRYPY_VERSION="18.6.1"

LABEL maintainer="Yves Vindevogel (vindevoy) - yves.vindevogel@asynchrone.com"

RUN apt-get update -y
RUN apt-get dist-upgrade -y

# Debian 10 did not yet have support for Python 3.8, staying on 3.7

RUN apt-get install python3.7 --no-install-recommends -y
RUN apt-get install python3-pip --no-install-recommends -y

RUN pip3 install cherrypy==$CHERRYPY_VERSION

RUN apt-get autoremove
RUN apt-get clean all

RUN mkdir -p /opt/cherrypy

COPY resources/main.py /opt/cherrypy/main.py

EXPOSE 8080

WORKDIR /opt/cherrypy
CMD ["python3", "/opt/cherrypy/main.py"]

###
#
#   Version history
#
#	Yves Vindevogel (vindevoy)
#	2020-11-30
#
#	Basic Debian image with Python and CherryPy installed on it
#
###
