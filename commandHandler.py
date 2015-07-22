# encoding: UTF-8
__author__ = 'bakabie'
import requests,json
class worktileAPI():
	pass

class worktileUserAPI(worktileAPI):
	def GetUserInfo(self,token):
		t = requests.get("https://api.worktile.com/v1/user/profile",headers = {"access_token":token})
		if 'error_code' in t.text:
			return "error"
		else:
			return t.text

class worktileProjectAPI(worktileAPI):
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



	def Entry_GetTask(self,pid,token):
		if not pid or not token:
			return "no pid or token"
		else:
			data = {
				"pid":pid,
				"access_token":token
			}
			t = requests.get("https://api.worktile.com/v1/entries",data)
			if "error_code" in t.text:
				return "error"
			else:
				return t.text
	def Entry_CreateTask(self,pid,token,name):
		if not pid or not token or not name:
			return "error"
		else:
			data = {
				"name":name
			}
			t = requests.post("https://api.worktile.com/v1/entries?pid="+pid+"&access_token="+token)
			if "error_code" in t.text:
				return "error"
			else:
				return t.text
	def Entry_Rename(self,entry_id,pid,token,name):
		if not entry_id or not pid or not token or not name:
			return "error"
		else:
			data = {
				"name":name
			}
			t = requests.put("https://api.worktile.com/v1/entries/"+entry_id+"?pid="+pid+"&access_token="+token)
			if "error_code" in t.text:
				return "error"
			else:
				return t.text