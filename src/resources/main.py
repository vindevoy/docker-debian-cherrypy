###
#
#   Yves Vindevogel (vindevoy)
#   2020-11-30
#
#   HelloWorld in CherryPy
#
###

import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

# The server.socket_host is needed for running in a container
cherrypy.config.update({'server.socket_host': '0.0.0.0'})

cherrypy.quickstart(HelloWorld())
