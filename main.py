# coding=utf8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from GoingMerry import Application

define("port", default=8080, help="run on the given port", type=int)
define("address", default='0.0.0.0', help="listen on the given address", type=str)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port, options.address)
    print "[+] ThousandSunny is running on %s:%d" % (options.address, options.port)
    tornado.ioloop.IOLoop.instance().start()