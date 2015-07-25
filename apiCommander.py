# coding: UTF-8
from __future__ import unicode_literals
import pickledb
import requests
import commandHandler
from telebot import TeleBot
__author__ = 'BroncoTc'

bot = TeleBot(token="96054818:AAFiPFHafymEzsJx67ftJ0XFKe5pwlRKF3E")
appKey = "0ae48b66b7564a9fb2011138ed02fa21"
db = pickledb.load("./worktilebot.db", True)
tempDb=pickledb.load("./tempdata.db",False)

def oauthProcessor(user_id, forceReOauth=False):
	userWorktileToken = db.get(str(user_id) + "_worktileToken")
	if userWorktileToken == None or forceReOauth:
		requestData = {"client_id": appKey,
					   "redirect_uri": "https://broncotc.com:8443/bot/worktileOauth",
					   "state": str(user_id)}
		oauthUrl = requests.get("https://open.worktile.com/oauth2/authorize", params=requestData).url
		return [None, oauthUrl]
	else:
		return [userWorktileToken, None]


def commandRouter(msg, user_id, chat_id,worktileToken):
	if msg == "/start":
		oauthAddress = oauthProcessor(user_id, forceReOauth=True)[1]
		bot.send_message(chat_id, "你需要先授权（重新授权）本bot访问你的Worktile账户，点击此链接进行授权\n" + oauthAddress,disable_web_page_preview=True)
	elif msg == "/projects":
		project=commandHandler.worktileProjectAPI()
		projectList=project.getUserAllProject(token=worktileToken)
		print projectList
	elif msg == "":
		pass
	return 0
