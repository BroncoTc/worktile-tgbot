# encoding: UTF-8
__author__ = 'bakabie'
import requests
import json
#what the fffffff

class worktileUserAPI():
	def GetUserInfo(self, token):

		t = requests.get("https://api.worktile.com/v1/user/profile", params={"access_token": token})
		if 'error_code' in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

class worktileProjectAPI():
	def getUserAllProject(self, token):
		t = requests.get("https://api.worktile.com/v1/projects", params={"access_token": token})
		if 'error_code' in t.text:
			raise ValueError
		else:
			return json.dump(t.text)

	def getProjectDetail(self, pid, token):
		t = requests.get("https://api.worktile.com/v1/projects/" + pid, params={"access_token": token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def getProjectMember(self, pid, token):
		t = requests.get("https://api.worktile.com/v1/projects/" + pid + "/members", params={"access_token": token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def addProjectMember(self, pid, uid, role, token):
		data = {
			"uid": uid,
			"role": role,
			"access_token": token
		}
		t = requests.post("https://api.worktile.com/v1/projects/" + pid + "/members", data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def delProjectMember(self, pid, uid, token):
		t = requests.delete("https://api.worktile.com/v1/projects/" + pid + "/members/" + uid,
							headers={"access_token": token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)


class worktileEntryAPI():
	def getEntryTask(self, pid, token):
		data = {
			"pid": pid,
			"access_token": token
		}
		t = requests.get("https://api.worktile.com/v1/entries", params=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def createEntryTask(self, pid, token, name):
		data = {
			"name": name
		}
		t = requests.post("https://api.worktile.com/v1/entries",params={"pid" : pid ,"access_token" : token},data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def reEntryname(self, entry_id, pid, token, name):
		data = {
			"name": name
		}
		t = requests.put("https://api.worktile.com/v1/entries/" + entry_id ,params={ "pid" : pid , "access_token" : token},data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def watchEntryTask(self, entry_id, pid, token):
		t = requests.post(
			"https://api.worktile.com/v1/entries/" + entry_id + "/watcher",params={"pid" : pid , "access_token" : token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def delEntryTask(self, entry_id, pid, token):
		t = requests.delete(
			"https://api.worktile.com/v1/entries/" + entry_id , params={"pid" : pid , "access_token" : token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def reWatchEntryTask(self, entry_id, pid, token):
		t = requests.delete(
			"https://api.worktile.com/v1/entries/" + entry_id + "/watcher",params={"pid" : pid , "access_token" : token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)


class worktileTaskAPI():
	def getTaskList(self, token, pid, type):
		data = {
			"access_token": token,
			"pid": pid,
			"type": type
		}
		t = requests.get("https://api.worktile.com/v1/tasks", params=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def willOverTask(self, token):
		t = requests.get("https://api.worktile.com/v1/tasks/today",params={"access_token" : token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def createTask(self, pid, token, name, entry_id):
		data = {
			"name": name,
			"entry_id": entry_id
		}
		t = requests.post("https://api.worktile.com/v1/task",params={"pid" : pid , "access_token" : token},data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def taskDetail(self, pid, token, tid):
		t = requests.get("https://api.worktile.com/v1/tasks/" + tid , params={"access_token" : token , "pid" : pid})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def editTask(self, tid, pid, token, name, desc):
		data = {
			"name": name,
			"desc": desc
		}
		t = requests.put("https://api.worktile.com/v1/tasks/" + tid , params = {"pid" : pid ,"access_token" : token},data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def deleteTask(self, tid, pid, token):
		t = requests.delete("https://api.worktile.com/v1/tasks/" + tid ,params={"pid" : pid , "access_token" : token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def movTask(self,tid,pid,token,to_pid,to_entry_id):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/move",params={"pid":pid,"access_token":token},data ={"to_pid":to_pid,"to_entry_id":to_entry_id})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def setEnpiryDate(self,tid,pid,token,expire):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/expire",params = {"pid":pid,"access_token":token},data={"expire":expire})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def allotTask(self,tid,pid,token,uid):
		t = requests.post("https://api.worktile.com/v1/tasks/"+tid+"/member",params = {"pid":pid,"access_token":token},data={"uid":uid})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def reAllotTask(self,tid,member_id,pid):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/members/"+member_id,params = {"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def addWatchTask(self,tid,pid,token,uids):
		t = requests.post("https://api.worktile.com/v1/tasks/"+tid+"/watcher",params = {"pid":pid,"access_token":token},data={"uids":uids})
		#this uids is a task:
		# curl -d 'uids=['abcea', 'abcd']' 'https://api.worktile.com/v1/tasks/adsa7sa6/watcher?pid=xxx&access_token=xxx'
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def reWatchTask(self,tid,uid,pid,token):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/watchers/"+uid,params={"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def setLabels(self,tip,pid,token,label):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"labels",params={"pid":pid,"access_token":token},data={"label":label})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def deleteLabels(self,tid,pid,label,token):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/labels",params={"pid":pid,"label":label,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def completeTask(self,tid,pid,token):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/complete",params={"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def unCompleteTask(self,tid,pid,token):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/uncomplete",params={"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def addToDo(self,tid,pid,token,name):
		t = requests.post("https://api.worktile.com/v1/tasks/"+tid+"/todo",params={"pid":pid,"access_token":token},data={"name":name})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def editTDo(self,tid,todo_id,pid,token,name):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/todos/"+todo_id,params={"pid":pid,"access_token":token},data={"name":name})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def completeToDo(self,tid,todo_id,pid,token):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/todos/"+todo_id+"/checked",params={"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def unCompleteToDo(self,tid,todo_id,pid,token):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/todos/"+todo_id+"/unchecked",params={"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def delToDo(self,tid,todo_id,pid,token):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/todos/"+todo_id,params={"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def getTaskArchived(self,pid,page,size,token):
		t = requests.get("https://api.worktile.com/v1/tasks/archived",params={"pid":pid,"page":page,"size":size,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def archiveEntryTask(self,pid,token,entry_id):
		t = requests.put("https://api.worktile.com/v1/tasks/archive",params={"pid":pid,"access_token":token},data={"entry_id":entry_id})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def archiveTask(self,tid,pid,token):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/archive",params={"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def unArchiveTask(self,tid,pid,entry_id,token):
		t = requests.put("https://api.worktile.com/v1/tasks/"+tid+"/unarchive",params={"pid":pid,"access_token":token},data={"entry_id":entry_id})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def getComments(self,tid,token,pid):
		t = requests.get("https://api.worktile.com/v1/tasks/"+tid+"/comments",params={"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def addComments(self,tid,pid,token,msg,fids):
		t = requests.post("https://api.worktile.com/v1/tasks/"+tid+"/comment",params={"pid":pid,"access_token":token},data={"message":msg,"fids":fids})
		#warning the rids is a list
		#curl -d 'message=评论的内容&fids=['adihzxx', 'adiiihhhxx']' 'https://api.worktile.com/v1/tasks/adsa7sa6/comment?pid=xxx&access_token=xxx'
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)
	def deleteComment(self,tid,cid,pid,token):
		t = requests.delete("https://api.worktile.com/v1/tasks/"+tid+"/comments/"+cid,params={"pid":pid,"access_token":token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)