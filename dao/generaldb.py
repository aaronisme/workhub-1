"""
Statement:
    Database connection info

Author:
    Will

Date:
    2014.11.05
"""



from tornado.options import define, options
import torndb


#---------------------Database info--------------------------------------------
define("port", default=8888, help="Run it on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="Database host")
define("mysql_database", default="workhub", help="Database name")
define("mysql_user", default="workhub", help="Database user")
define("mysql_password", default="Passw0rd", help="Database password, should be encrypted")


class ConnectDB():
    def __init__(self):
        # Have one global db connection across all handlers

        self.db = torndb.Connection(
            host=options.mysql_host,
            database=options.mysql_database,
            user=options.mysql_user,
            password=options.mysql_password
        )
        print 'Connect to database: workhub'


    def getdbinstance(self):
        return self.db