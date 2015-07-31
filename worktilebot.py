# encoding: UTF-8
from __future__ import unicode_literals
from flask import Flask, request
from commandParser import *
import requests
import pickledb
import json
import apiCommander
from telebot import TeleBot

global token
token = "96054818:AAFiPFHafymEzsJx67ftJ0XFKe5pwlRKF3E"
app = Flask(__name__)
db = pickledb.load("worktilebot.db", True)
bot = TeleBot(token=token)
appKey = "0ae48b66b7564a9fb2011138ed02fa21"


@app.before_first_request
def setWebhook():
	requests.get(
		"https://api.telegram.org/bot" + token + "/setWebhook?url=https://test.broncotc.com:8443/bot/webhook" + token)


@app.route('/bot/webhook' + token, methods=["POST"])
def telegramWebhookHandler():
	if request.method == "POST":
		incoming = request.get_json()
		chat_id = incoming['message']['chat']['id']
		msg = incoming['message']['text']
		user_id = incoming['message']['from']['id']
		commandContent = commandParser(msg)
		if (db.get(str(user_id) + "_worktileToken") != None) or (commandContent == "/start"):
			apiCommander.commandRouter(commandContent, user_id, chat_id, db.get(str(user_id) + "_worktileToken"))
		else:
			bot.send_message(chat_id, "请先私聊本bot以给予本bot访问你Worktile账户的权限")
		return '{"status":"ok"}'


@app.route('/bot/worktileAuthorizeOauth')
def oauthAuthorizeHandler():
	user_id = request.args["state"]
	oauthAuthorizeCode = request.args["code"]
	data = {"client_id": appKey, "code": oauthAuthorizeCode}
	oauthAccessTokenFeedback = requests.post("https://api.worktile.com/oauth2/access_token", data).text
	oauthAccessToken = json.loads((oauthAccessTokenFeedback))["access_token"]
	oauthRefreshToken = json.loads((oauthAccessTokenFeedback))["refresh_token"]
	db.set(str(user_id) + "_worktileAccessToken", oauthAccessToken)
	db.set(str(user_id) + "_worktileRefreshToken", oauthRefreshToken)
	return '{"status":"ok"}'


if __name__ == '__main__':
	sslcontext = ('all.crt', 'all.key')
	app.run(host="0.0.0.0", port=8443, ssl_context=sslcontext)
