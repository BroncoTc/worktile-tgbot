# coding: UTF-8
from __future__ import unicode_literals
from flask import Flask,request
app=Flask(__name__)

@app.route("/")
def webhookhandler():
	pass

if __name__=="__main__":
	app.run(host="broncotc.com",port="443")