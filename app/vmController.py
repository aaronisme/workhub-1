"""
Statement:
    Create the vm route handler
Author:
    Will
Date:
    2014.11.12
"""

#-*-coding: utf-8 -*-

import app.basehandler

class VmPlanHandler(app.basehandler.BaseHandler):
    def get(self):
        #response = None
        self.render("vm.html")

