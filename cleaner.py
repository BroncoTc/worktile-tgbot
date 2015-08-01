# encoding: UTF-8
from __future__ import unicode_literals
__author__ = 'broncotc'
from flask import Flask
import requests

token = "96054818:AAFiPFHafymEzsJx67ftJ0XFKe5pwlRKF3E"
app = Flask(__name__)
requests.get("https://api.telegram.org/bot" + token + "/setWebhook?url=https://broncotc.com:8443/bot/webhook" + token)


@app.route('/bot/webhook' + token, methods=["POST"])
def telegramWebhookHandler():
	return '{"status":"ok"}'

if __name__ == '__main__':
	sslcontext = ('all.crt', 'all.key')
	app.run(host="0.0.0.0", port=8443, ssl_context=sslcontext)
