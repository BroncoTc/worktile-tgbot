# encoding: UTF-8
__author__ = 'bakabie'
import requests
import json
class worktileUserAPI():
	def GetUserInfo(self, token):

		t = requests.get("https://api.worktile.com/v1/user/profile", params={"access_token": token})
		if 'error_code' in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
class worktileProjectAPI():
	def __init__(self,token):
		self.token = token
	def getUserAllProject(self):
		t = requests.get("https://api.worktile.com/v1/projects", params={"access_token": self.token})
		if 'error_code' in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def getProjectDetail(self, pid):
		t = requests.get("https://api.worktile.com/v1/projects/" + pid, params={"access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def getProjectMember(self, pid):
		t = requests.get("https://api.worktile.com/v1/projects/" + pid + "/members", params={"access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def addProjectMember(self, pid, uid, role):
		data = {
			"uid": uid,
			"role": role,
			"access_token": self.token
		}
		t = requests.post("https://api.worktile.com/v1/projects/" + pid + "/members", data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def delProjectMember(self, pid, uid):
		t = requests.delete("https://api.worktile.com/v1/projects/" + pid + "/members/" + uid,
							headers={"access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
class worktileEntryAPI():
	def __init__(self,token):
		self.token=token
	def getEntryTask(self, pid):
		data = {
			"pid": pid,
			"access_token": self.token
		}
		t = requests.get("https://api.worktile.com/v1/entries", params=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def createEntryTask(self, pid, name):
		data = {
			"name": name
		}
		t = requests.post("https://api.worktile.com/v1/entries",params={"pid" : pid ,"access_token" : self.token},data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def reEntryname(self, entry_id, pid, name):
		data = {
			"name": name
		}
		t = requests.put("https://api.worktile.com/v1/entries/" + entry_id ,params={ "pid" : pid , "access_token" : self.token},data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def watchEntryTask(self, entry_id, pid):
		t = requests.post(
			"https://api.worktile.com/v1/entries/" + entry_id + "/watcher",params={"pid" : pid , "access_token" : self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def delEntryTask(self, entry_id, pid):
		t = requests.delete(
			"https://api.worktile.com/v1/entries/" + entry_id , params={"pid" : pid , "access_token" : self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def reWatchEntryTask(self, entry_id, pid):
		t = requests.delete(
			"https://api.worktile.com/v1/entries/" + entry_id + "/watcher",params={"pid" : pid , "access_token" : self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
class worktileTaskAPI():
	def __init__(self,token):
		self.token=token
	def getTaskList(self, pid, type):
		data = {
			"access_token": self.token,
			"pid": pid,
			"type": type
		}
		t = requests.get("https://api.worktile.com/v1/tasks", params=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def willOverTask(self):
		t = requests.get("https://api.worktile.com/v1/tasks/today",params={"access_token" : self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def createTask(self, pid, name, entry_id):
		data = {
			"name": name,
			"entry_id": entry_id
		}
		t = requests.post("https://api.worktile.com/v1/task",params={"pid" : pid , "access_token" : self.token},data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def taskDetail(self, pid, tid):
		t = requests.get("https://api.worktile.com/v1/tasks/" + tid , params={"access_token" : self.token , "pid" : pid})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def editTask(self, tid, pid, name, desc):
		data = {
			"name": name,
			"desc": desc
		}
		t = requests.put("https://api.worktile.com/v1/tasks/" + tid , params = {"pid" : pid ,"access_token" : self.token},data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def deleteTask(self, tid, pid):
		t = requests.delete("https://api.worktile.com/v1/tasks/" + tid ,params={"pid" : pid , "access_token" : self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def movTask(self,tid,pid,to_pid,to_entry_id):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/move",params={"pid":pid,"access_token":self.token},data ={"to_pid":to_pid,"to_entry_id":to_entry_id})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def setEnpiryDate(self,tid,pid,expire):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/expire",params = {"pid":pid,"access_token":self.token},data={"expire":expire})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def allotTask(self,tid,pid,uid):
		t = requests.post("https://api.worktile.com/v1/tasks/"+tid+"/member",params = {"pid":pid,"access_token":self.token},data={"uid":uid})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def reAllotTask(self,tid,member_id,pid):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/members/"+member_id,params = {"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def addWatchTask(self,tid,pid,uids):
		t = requests.post("https://api.worktile.com/v1/tasks/"+tid+"/watcher",params = {"pid":pid,"access_token":self.token},data={"uids":uids})
		#this uids is a task:
		# curl -d 'uids=['abcea', 'abcd']' 'https://api.worktile.com/v1/tasks/adsa7sa6/watcher?pid=xxx&access_token=xxx'
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def reWatchTask(self,tid,uid,pid):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/watchers/"+uid,params={"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def setLabels(self,tip,pid,label):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"labels",params={"pid":pid,"access_token":self.token},data={"label":label})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def deleteLabels(self,tid,pid,label):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/labels",params={"pid":pid,"label":label,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def completeTask(self,tid,pid):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/complete",params={"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def unCompleteTask(self,tid,pid):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/uncomplete",params={"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def addToDo(self,tid,pid,name):
		t = requests.post("https://api.worktile.com/v1/tasks/"+tid+"/todo",params={"pid":pid,"access_token":self.token},data={"name":name})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def editTDo(self,tid,todo_id,pid,name):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/todos/"+todo_id,params={"pid":pid,"access_token":self.token},data={"name":name})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def completeToDo(self,tid,todo_id,pid):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/todos/"+todo_id+"/checked",params={"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def unCompleteToDo(self,tid,todo_id,pid):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/todos/"+todo_id+"/unchecked",params={"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def delToDo(self,tid,todo_id,pid):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/todos/"+todo_id,params={"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def getTaskArchived(self,pid,page,size):
		t = requests.get("https://api.worktile.com/v1/tasks/archived",params={"pid":pid,"page":page,"size":size,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def archiveEntryTask(self,pid,entry_id):
		t = requests.put("https://api.worktile.com/v1/tasks/archive",params={"pid":pid,"access_token":self.token},data={"entry_id":entry_id})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def archiveTask(self,tid,pid):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/archive",params={"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def unArchiveTask(self,tid,pid,entry_id):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/unarchive",params={"pid":pid,"access_token":self.token},data={"entry_id":entry_id})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def getComments(self,tid,pid):
		t = requests.get("https://api.worktile.com/v1/tasks/"+tid+"/comments",params={"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def addComments(self,tid,pid,msg,fids):
		t = requests.post("https://api.worktile.com/v1/tasks/"+tid+"/comment",params={"pid":pid,"access_token":self.token},data={"message":msg,"fids":fids})
		#warning the rids is a list
		#curl -d 'message=评论的内容&fids=['adihzxx', 'adiiihhhxx']' 'https://api.worktile.com/v1/tasks/adsa7sa6/comment?pid=xxx&access_token=xxx'
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def deleteComment(self,tid,cid,pid):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/comments/"+cid,params={"pid":pid,"access_token":self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)