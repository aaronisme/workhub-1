"""
Statement:
    To handle the user info validation
Author:
    Will
Date:
    2014.11.06
"""
# -*- coding: utf-8 -*-
from dao.userinfo import UserInfoDao
class UserService():
    # To validate the email address, password... We do NOT validate the format, it should be
    # checked in the page side.
    def validate_logon(self, email, password):
        userinfodao = UserInfoDao()
        users = userinfodao.getAllUser()
        if users:
            for user in users:
                if user.email != email:
                    continue
                print 'Valid email:  %s' % email
                print 'valid id: %d' % user.id
                pwd = userinfodao.getPasswordById(user.id)
                if pwd[0].password == password:
                    print 'Valid password:   ******'
                    return user
                else:
                    print 'Invalid password.'
                    return None
            print 'Invalid email:  %s' % email
            return None

    def validate_register(self, email, username, password, group):
        userinfodao = UserInfoDao()
        users = userinfodao.getAllUser()
        if users:
            for user in users:
                if user.email != email:
                    continue
                else:
                    return None
