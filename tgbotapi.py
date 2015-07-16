# coding: UTF-8
__author__ = "BroncoTc"
import requests
class bot(object):
	def __init__(self, token):
		try:
			global urlbase
			urlbase = "https://api.telegram.org/bot" + str(token) + "/"
		except:
			pass

	def send(self, target_ID, text):
		try:
			postContent = {"chat_id": str(target_ID), "text": text}
			return requests.post(url=urlbase + "sendMessage", data=postContent)
		except:
			pass

	def receive(self, offset=0, limit=100):
		try:
			payload = {"offset": offset, "limit": limit}
			messages = requests.get(urlbase + "getUpdates", params=payload)
			messagesjson = messages.json()
			return messagesjson
		except:
			return
