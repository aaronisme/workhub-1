"""
*************************************************************************************
*   Statement:
        JS will request the data from this handler to render page through Ajax
*   Author:
        Will
*   Date:
        2014.11.14
*   Comment:
        Fake data to test the data communication
*************************************************************************************
"""



# -*- coding: utf-8 -*-

import app.basehandler
import json
class DataHandler(app.basehandler.BaseHandler):

    def post(self):

        para = self.get_query_argument("key")
        print 'Ajax get from key: %s' % para
        if para == "vm":
            response = {
                "response": True,
	            "hasData": True,
	            "tabName":"id,ip,user,Occupied,Build,Description",
	            "data" : [
		                    [1,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		                    [2,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		                    [3,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		                    [4,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		                    [5,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		                    [6,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		                    [7,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		                    [8,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"],
		                    [9,"9.110.94.110:8080","QC","M18","10.2.1003.156","Capsian xxx"]
	    ]
            }
        elif para == "builds":
            response = {
                "Info": "No test info here"
            }
        else:
            response = {
                "error": "error"
            }
        self.write(json.dumps(response))
