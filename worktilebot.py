# encoding: UTF-8
from __future__ import unicode_literals
from flask import Flask,request
from telebot import TeleBot
import requests
import pickledb
import commandHandler

global token
token="96054818:AAFiPFHafymEzsJx67ftJ0XFKe5pwlRKF3E"
app = Flask(__name__)
bot=TeleBot(token=token)
db=pickledb.load("./worktilebot.db",False)

@app.before_first_request
def setwebhook():
	requests.get("https://api.telegram.org/bot"+token+"/setWebhook?url=https://broncotc.com:8443/bot/webhook"+token)

@app.route('/bot/webhook'+token,methods=["POST"])
def telegramwebhookhandler():
	if request.method=="POST":
		incoming=request.get_json()
		print incoming
		chat_id = incoming['message']['chat']['id']
		msg =incoming['message']['text']
		user_id=incoming['message']['from']['id']


		return '{"status":"ok"}'
@app.route('/bot/worktileoatuh')
def oauthHandler():
	pass


if __name__ == '__main__':
	sslcontext = ('all.crt', 'all.key')
	app.run(host="0.0.0.0",port=8443,ssl_context=sslcontext)