# encoding: UTF-8
__author__ = 'bakabie'
import requests,json

class worktileUserAPI():
	def GetUserInfo(self,token):
		t = requests.get("https://api.worktile.com/v1/user/profile",headers = {"access_token":token})
		if 'error_code' in t.text:
			return "error"
		else:
			return t.text

class worktileProjectAPI():
	def getUserAllProject(self,token):
			t = requests.get("https://api.worktile.com/v1/projects",headers = {"access_token":token})
			if 'error_code' in t.text:
				return "error"
			else:
				return t.text
	def getDetail(self,pid,token):
		t = requests.get("https://api.worktile.com/v1/projects/"+pid,headers = {"access_token":token})
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def getMember(self,pid,token):
		t= requests.get("https://api.worktile.com/v1/projects/"+pid+"/members",headers = {"access_token":token})
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def addMember(self,pid,uid,role,token):
		data={
			"uid":uid,
			"role":role,
			"access_token":token
		}
		t = requests.post("https://api.worktile.com/v1/projects/"+pid+"/members",data=data)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def delMember(self,pid,uid,token):
		t = requests.delete("https://api.worktile.com/v1/projects/"+pid+"/members/"+uid,headers={"access_token":token})
		if "error_code" in t.text:
			return "error"
		else:
			return t.text

class worktileEntryAPI():
	def getTask(self,pid,token):
		data = {
			"pid":pid,
			"access_token":token
		}
		t = requests.get("https://api.worktile.com/v1/entries",data)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def createTask(self,pid,token,name):
		data = {
			"name":name
		}
		t = requests.post("https://api.worktile.com/v1/entries?pid="+pid+"&access_token="+token)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def rename(self,entry_id,pid,token,name):
		data = {
			"name":name
		}
		t = requests.put("https://api.worktile.com/v1/entries/"+entry_id+"?pid="+pid+"&access_token="+token)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text