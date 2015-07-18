from flask import Flask,request
from telebot import TeleBot
import requests
import pickledb

global token
token="96054818:AAFiPFHafymEzsJx67ftJ0XFKe5pwlRKF3E"
app = Flask(__name__)
bot=TeleBot(token=token)

@app.before_first_request
def setwebhook():
	requests.get("https://api.telegram.org/bot"+token+"/setWebhook?url=https://broncotc.com:8443/bot/webhook"+token)

@app.route('/bot/webhook'+token,methods=["POST"])
def telegramwebhookhandler():
	if request.method=="POST":
		incoming=request.get_json()
		chat_id = incoming[u'message'][u'chat'][u'id']
		msg =incoming[u'message'][u'text']
		bot.send_message(chat_id=chat_id,text=msg)
		return '{"status":"ok"}'
	else:
		return '{"status":"ok"}'

if __name__ == '__main__':
	sslcontext = ('all.crt', 'all.key')
	app.run(host="broncotc.com",port=8443,ssl_context=sslcontext)