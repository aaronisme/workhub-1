"""
Statement:
    This file is used to init the app, including the following:
    1.Define the database info
    2.Define the handler to route
    3.Build up the server

Author:
    Will

Date:
    2014.11.02
"""
#---------------------------------------------------------------------------
#-*- coding: utf-8 -*-
import os
import uuid
import base64

import tornado.options
from tornado.options import options
import tornado.web
import tornado.httpserver
import tornado.ioloop

import app.userController
from dao.generaldb import ConnectDB
import app.vmController
import app.dataController

class HubApplication(tornado.web.Application):
    def __init__(self):
        # Handler to route
        handlers = [
            (r"/", app.userController.IndexHandler),
            (r"/user/register", app.userController.RegisterHandler),
            (r"/user/login", app.userController.LoginHandler),
            (r"/user/logout", app.userController.LogoutHandler),
            (r"/vm", app.vmController.VmPlanHandler),
            (r"/getData", app.dataController.DataHandler)
        ]
        # Settings for this app
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            # Use UUID to generate cookie secret
            cookie_secret=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
            login_url="user/login",
            debug=True,
        )

        # Call the parent init function
        tornado.web.Application.__init__(self, handlers, **settings)

        # Connect to the database and create a global instance
        self.db = ConnectDB().getdbinstance()


def startserver():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(HubApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    http_server.close_all_connections()


if __name__ == "__main__":
    startserver()