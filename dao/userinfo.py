"""
Statement:
    Fetch the database info from user, userdetail, password, group


Author:
    Will

Date:
    2014.11.05
"""

from workhub import HubApplication
from generaldb import ConnectDB
class UserInfoDao():
    def __init__(self):
        self.db = ConnectDB().getdbinstance()

    def getNameById(self, userid):
        result = self.db.query("select name from workhub.user where id = %s ", userid)

        if result:
            return result
        else:
            print 'No query result!'
            return None


    def getEmailById(self, userid):
        result = self.db.query("select email from workhub.user where id = %s", userid)

        if result:
            return result
        else:
            print 'No query result!'
            return None


    def getAllUser(self):
        result = self.db.query("select * from workhub.user")

        if result:
            return result
        else:
            print 'No query result in user'
            return None

    def createUser(self, username, email, password, group):
        pass
    # userdetail
    def getGroupById(self, userid):
        result = self.db.query("select group from workhub.userdetail where id = %s", userid )

        if result:
            return result
        else:
            print 'No query result!'
            return None


    def getCreatetimeById(self, userid):
        result = self.db.query("select group from workhub.createtime where id = %s", userid)

        if result:
            return result
        else:
            print 'No query result!'
            return None


    def getAllUserDetail(self):
        result = self.db.query("select * from workhub.createtime")

        if result:
            return result
        else:
            print 'No query result!'
            return None


    # password
    def getPasswordById(self, userid):
        result = self.db.query("select password from workhub.password where userid = %s", userid)

        if result:
            return result
        else:
            print 'No query result!'
            return None

    # group
    def getGroupNameById(self, userid):
        result = self.db.query("select group from workhub.groupname where id = %s", userid)

        if result:
            return result
        else:
            print 'No query result!'
            return None