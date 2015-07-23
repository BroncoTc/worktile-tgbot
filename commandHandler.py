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


class worktileEntryAPI
	def GetTask(self,pid,token):
		data = {
			"pid":pid,
			"access_token":token
		}
		t = requests.get("https://api.worktile.com/v1/entries",data)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def CreateTask(self,pid,token,name):
		data = {
			"name":name
		}
		t = requests.post("https://api.worktile.com/v1/entries?pid="+pid+"&access_token="+token)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def Rename(self,entry_id,pid,token,name):
		data = {
			"name":name
		}
		t = requests.put("https://api.worktile.com/v1/entries/"+entry_id+"?pid="+pid+"&access_token="+token)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def WatchTask(self,entry_id,pid,token):
		t = requests.post("https://api.worktile.com/v1/entries/"+entry_id+"/watcher?pid="+pid+"&access_token="+token)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def DelTask(self,entry_id,pid,token):
		t = requests.delete("https://api.worktile.com/v1/entries/"+entry_id+"?pid="+pid+"&access_token="+token)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def ReWatchTask(self,entry_id,pid,token):
		t =requests.delete("https://api.worktile.com/v1/entries/"+entry_id+"/watcher?pid="+pid+"&access_token="+token)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
class worktileTaskAPI():
	def GetTaskList(self,token,pid,type):
		data = {
			"access_token":token,
			"pid":pid,
			"type":type
		}
		t = requests.get("https://api.worktile.com/v1/tasks",data = data)
		if "error_code" in t.text:
			return "error"
		else:
			return t.text
	def WillOverTask(self,token):
		t= requests.get("https://api.worktile.com/v1/tasks/today?access_token="+token)
		if "error_code" in t.text
			return "error"
		else:
			return t.text
	def CreatNewTask(self,pid,token,name,entry_id):
		data = {
			"name":name,
			"entry_id":entry_id
		}
		t=requests.post("https://api.worktile.com/v1/task?pid="+pid+"&access_token="+token)
		if "error_code" in t.text
			return "error"
		else:
			return t.text
	def TaskDet(self,pid,token,tid):
		t=requests.get("https://api.worktile.com/v1/tasks/"+tid+"?access_token="+token+"&pid="+pid)
		if "error_code" in t.text
			return "error"
		else:
			return t.text
	def ReTask(self,tid,pid,token,name,desc):
		data = {
			"name":name,
			"desc":desc
		}
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"?pid="+pid+"&access_token="+token)