# coding: UTF-8
from __future__ import unicode_literals
import pickledb
import requests

__author__ = 'BroncoTc'
appKey="0ae48b66b7564a9fb2011138ed02fa21"
db=pickledb.load("./worktilebot.db",False)
def oauthProcessor(user_id):
	userWorktileToken=db.get(str(user_id)+"_worktileToken")
	if userWorktileToken!=None:
		return [userWorktileToken,None]
	else:
		requestData={"client_id":appKey,
					 "redirect_uri":"https://broncotc.com:8443/bot/worktileOauth",
					 "state":str(user_id)}
		oauthUrl=requests.get("https://open.worktile.com/oauth2/authorize",params=requestData).url
		return [None,oauthUrl]
def commandRouter(commandString,user_id,chat_id):
	pass
