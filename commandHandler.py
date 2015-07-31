# encoding: UTF-8
__author__ = ['bakabie',"BroncoTc"]
import requests
import json


class worktileUser():
	def	__init__(self,token):
		self.token=token
	def GetUserInfo(self, token):
		t = requests.get("https://api.worktile.com/v1/user/profile", params={"access_token": token})
		if 'error_code' in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def getUserAllProject(self):
		t = requests.get("https://api.worktile.com/v1/projects", params={"access_token": self.token})
		if 'error_code' in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def willOverTask(self):
		t = requests.get("https://api.worktile.com/v1/tasks/today", params={"access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)


class worktileProject():
	def __init__(self, token, pid):
		self.token = token
		self.pid = pid

	def getProjectDetail(self):
		t = requests.get("https://api.worktile.com/v1/projects/" + self.pid, params={"access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def getProjectMember(self):
		t = requests.get("https://api.worktile.com/v1/projects/" + self.pid + "/members",
						 params={"access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def addProjectMember(self, uid, role):
		data = {
			"uid": uid,
			"role": role,
			"access_token": self.token
		}
		t = requests.post("https://api.worktile.com/v1/projects/" + self.pid + "/members", data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def delProjectMember(self, uid):
		t = requests.delete("https://api.worktile.com/v1/projects/" + self.pid + "/members/" + uid,
							headers={"access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def getEntryList(self, pid):
		data = {
			"pid": pid,
			"access_token": self.token
		}
		t = requests.get("https://api.worktile.com/v1/entries", params=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def getTaskList(self, type):
		data = {
			"access_token": self.token,
			"pid": self.pid,
			"type": type
		}
		t = requests.get("https://api.worktile.com/v1/tasks", params=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def createEntry(self, name):
		data = {
			"name": name
		}
		t = requests.post("https://api.worktile.com/v1/entries", params={"pid": self.pid, "access_token": self.token},
						  data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

class worktileEntry(worktileProject):
	def __init__(self, entry_id):
		self.entry_id = entry_id

	def renameEntry(self, name):
		data = {
			"name": name
		}
		t = requests.put("https://api.worktile.com/v1/entries/" + self.entry_id,
						 params={"pid": self.pid, "access_token": self.token}, data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def watchEntry(self):
		t = requests.post(
			"https://api.worktile.com/v1/entries/" + self.entry_id + "/watcher",
			params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def deleteEntry(self):
		t = requests.delete(
			"https://api.worktile.com/v1/entries/" + self.entry_id,
			params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def stopWatchEntry(self):
		t = requests.delete(
			"https://api.worktile.com/v1/entries/" + self.entry_id + "/watcher",
			params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
	def archiveEntry(self):
		t = requests.put("https://api.worktile.com/v1/tasks/archive",
						 params={"pid": self.pid, "access_token": self.token}, data={"entry_id": self.entry_id})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)


class worktileTask(worktileEntry):
	def __init__(self, tid):
		self.tid = tid





	def createTask(self, name):
		data = {
			"name": name,
			"entry_id": self.entry_id
		}
		t = requests.post("https://api.worktile.com/v1/task", params={"pid": self.pid, "access_token": self.token},
						  data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def taskDetail(self):
		t = requests.get("https://api.worktile.com/v1/tasks/" + self.tid,
						 params={"access_token": self.token, "pid": self.pid})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def editTask(self, name, desc):
		data = {
			"name": name,
			"desc": desc
		}
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid,
						 params={"pid": self.pid, "access_token": self.token}, data=data)
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def deleteTask(self):
		t = requests.delete("https://api.worktile.com/v1/tasks/" + self.tid,
							params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def movTask(self, to_pid, to_entry_id):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "/move",
						 params={"pid": self.pid, "access_token": self.token},
						 data={"to_pid": to_pid, "to_entry_id": to_entry_id})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def setEnpiryDate(self, expire):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "/expire",
						 params={"pid": self.pid, "access_token": self.token}, data={"expire": expire})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def allotTask(self, uid):
		t = requests.post("https://api.worktile.com/v1/tasks/" + self.tid + "/member",
						  params={"pid": self.pid, "access_token": self.token}, data={"uid": uid})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def reAllotTask(self, member_id):
		t = requests.delete("https://api.worktile.com/v1/tasks/" + self.tid + "/members/" + member_id,
							params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def addWatchTask(self, uids):
		t = requests.post("https://api.worktile.com/v1/tasks/" + self.tid + "/watcher",
						  params={"pid": self.pid, "access_token": self.token}, data={"uids": uids})
		# this uids is a task:
		# curl -d 'uids=['abcea', 'abcd']' 'https://api.worktile.com/v1/tasks/adsa7sa6/watcher?pid=xxx&access_token=xxx'
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def stopWatchTask(self, uid):
		t = requests.delete("https://api.worktile.com/v1/tasks/" + self.tid + "/watchers/" + uid,
							params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def setLabels(self, label):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "labels",
						 params={"pid": self.pid, "access_token": self.token}, data={"label": label})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def deleteLabels(self, label):
		t = requests.delete("https://api.worktile.com/v1/tasks/" + self.tid + "/labels",
							params={"pid": self.pid, "label": label, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def completeTask(self):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "/complete",
						 params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def unCompleteTask(self):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "/uncomplete",
						 params={"pid": self.pidpid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def addToDo(self, name):
		t = requests.post("https://api.worktile.com/v1/tasks/" + self.tid + "/todo",
						  params={"pid": self.pid, "access_token": self.token}, data={"name": name})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def editToDo(self, todo_id, name):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "/todos/" + todo_id,
						 params={"pid": self.pid, "access_token": self.token}, data={"name": name})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def completeToDo(self, todo_id):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "/todos/" + todo_id + "/checked",
						 params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def unCompleteToDo(self, todo_id):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "/todos/" + todo_id + "/unchecked",
						 params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def deleteToDo(self, todo_id):
		t = requests.delete("https://api.worktile.com/v1/tasks/" + self.tid + "/todos/" + todo_id,
							params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def getTaskArchived(self, page, size):
		t = requests.get("https://api.worktile.com/v1/tasks/archived",
						 params={"pid": self.pid, "page": page, "size": size, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)



	def archiveTask(self):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "/archive",
						 params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def unArchiveTask(self):
		t = requests.put("https://api.worktile.com/v1/tasks/" + self.tid + "/unarchive",
						 params={"pid": self.pid, "access_token": self.token}, data={"entry_id": self.entry_id})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def getComments(self):
		t = requests.get("https://api.worktile.com/v1/tasks/" + self.tid + "/comments",
						 params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def addComments(self, msg, fids):
		t = requests.post("https://api.worktile.com/v1/tasks/" + self.tid + "/comment",
						  params={"pid": self.pid, "access_token": self.token}, data={"message": msg, "fids": fids})
		# warning the rids is a list
		# curl -d 'message=评论的内容&fids=['adihzxx', 'adiiihhhxx']' 'https://api.worktile.com/v1/tasks/adsa7sa6/comment?pid=xxx&access_token=xxx'
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)

	def deleteComment(self, cid):
		t = requests.delete("https://api.worktile.com/v1/tasks/" + self.tid + "/comments/" + cid,
							params={"pid": self.pid, "access_token": self.token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.loads(t.text)
