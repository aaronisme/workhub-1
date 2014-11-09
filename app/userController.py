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
        js = None
        try:
            js = json.loads(self.request.body)
            if "username" not in js or "password" not in js or "email" not in js:
                raise ValueError("Request parameter is not valid")
        except Exception:
            self.write_error(403, error="Request parameter is not valid")
            return
        result, msg = Validator.validate_username(js['username']) 
        if not result: 
            self.write_error(403, error=msg)
            return
        else:
            #check if username exists
            if self.db.get("SELECT * FROM users WHERE username = %s", js['username']):
                self.write_error(403, error="Request parameter is not valid")
                return
        result, msg = Validator.validate_email(js['email'])
        if not result:
            self.write_error(403, error=msg)
            return
        else:
            #check if email exists
            if self.db.get("SELECT * FROM users WHERE email = %s", js['email']):
                self.write_error(403, error="The email address has been registered")
                return
        result, msg = Validator.validate_password(js['password'])
        if not result:
            self.write_error(403, error=msg)
        #creat the user by inserting into db
        curtime = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        user_id = self.db.execute(
            "INSERT INTO users "
            "(username, email, password, last_login, created, updated)"
            "VALUES(%s, %s, %s, %s, %s, %s)",
            js['username'], js['email'], js['password'], curtime, curtime, curtime
        )
        if not user_id:
            self.write_error(403, error="Fail to creating a user")
            return
        #create cookie for login
        self.set_secure_cookie("uid", str(user_id))
        response = {"uid":user_id,
                    "message":"New user created successful"}
        self.write(response)


class LoginHandler(app.basehandler.BaseHandler):
    def get(self):
        if not self.get_current_user():
            return self.render("login.html")
        else:
            # Should redirect to the current user main page
            self.render("user.html")

    def post(self):
        # Login by sending the following json to request body
        js = json.loads(self.request.body)
        if "email" in js and "password" in js:
            user = UserService().validate_logon(js['email'], js['password'])
            if user:
                #set secure cookie
                self.set_secure_cookie("uid", str(user.id))
                response = {"uid" : user.id, "message" : "Log on successfully"}
                self.write(response)
                return self.render("index.html")
        self.write_error(403, error="Invalid email address or password")
        self.render("error.html")


class LogoutHandler(app.basehandler.BaseHandler):
    def get(self):
        self.clear_cookie("uid")
        self.write({"message" : "Logout successfully"})
        

class IndexHandler(app.basehandler.BaseHandler):
    def get(self):
        return self.redirect("index.html")