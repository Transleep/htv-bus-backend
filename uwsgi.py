#!/usr/bin/env python
#coding:utf-8
# Author:  D.Z 
# Purpose: WSGI for backend
# Created: 01/07/2017


from server import app as application

if __name__=='__main__':
    application.run()