# encoding: UTF-8
from flask import Flask,request
from telebot import TeleBot
import requests
import pickledb

global token
token="96054818:AAFiPFHafymEzsJx67ftJ0XFKe5pwlRKF3E"
app = Flask(__name__)
bot=TeleBot(token=token)

db=pickledb.load("worktilebot.db",False)
db.set("author","BroncoTc/豆腐干")
db.dump()


@app.before_first_request
def setwebhook():
	requests.get("https://api.telegram.org/bot"+token+"/setWebhook?url=https://broncotc.com:8443/bot/webhook"+token)

@app.route('/bot/webhook'+token,methods=["POST"])
def telegramwebhookhandler():
	if request.method=="POST":
		incoming=request.get_json()
		chat_id = incoming[u'message'][u'chat'][u'id']
		msg =incoming[u'message'][u'text']

		return '{"status":"ok"}'

@app.route('/bot/worktileoatuh')
def oauthHandler():
	pass


if __name__ == '__main__':
	sslcontext = ('all.crt', 'all.key')
	app.run(host="0.0.0.0",port=8443,ssl_context=sslcontext)