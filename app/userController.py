"""
Statement:
    Create the use route handler
Author:
    Will
Date:
    2014.11.02
"""

# -*- coding: utf-8 -*-
import json
import re
import datetime
import tornado.gen
import tornado.web
import app.basehandler
from utils.validator import Validator
from service.userservice import UserService
class RegisterHandler(app.basehandler.BaseHandler):
    def post(self):
        #username, password, group
        email = self.get_argument("email")
        username = self.get_argument("username")
        password = self.get_argument("password")
        group = self.get_argument("group")

        # Check email
        user = UserService().validate_register(email, username, password, group)
        self.set_secure_cookie("userid", str(user.id))
        response = {"userid": user.id, "message": "New user created Succeed"}
        self.write(response)
        self.redirect('/')



class LoginHandler(app.basehandler.BaseHandler):
    def get(self):
        user = self.get_current_user()
        # Online now
        if user:
            self.redirect('/')
        else:
            self.write(json.dumps({'status': 'fail'}))
            self.render("login.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        user = UserService().validate_logon(username, password)
        if user:
            print 'Login successful'
            self.set_secure_cookie("userid", str(user.id))
            response = {"userid": user.id, "message": "Logon Succeed"}

            self.write(response)
            return self.redirect('/')
        else:
            print 'Login Failed'
            response = {"message": "Logon Failed"}
            self.write(response)
            return self.render('/user/login')



class LogoutHandler(app.basehandler.BaseHandler):
    #@tornado.web.authenticated
    def get(self):
        self.clear_cookie("userid")
        response = {"message": "Logout Succeed"}
        self.write(response)
        return self.redirect('/')
        

class IndexHandler(app.basehandler.BaseHandler):
    #@tornado.web.authenticated
    def get(self):
        self.render("index.html")