# encoding: UTF-8
__author__ = 'bakabie'
import requests
import json
#what the *****

class worktileUserAPI():
	def GetUserInfo(self, token):
		t = requests.get("https://api.worktile.com/v1/user/profile", params={"access_token": token})
		if 'error_code' in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

class worktileProjectAPI():
	def getUserAllProject(self, token):
		t = requests.get("https://api.worktile.com/v1/projects", headers={"access_token": token})
		print t
		print t.text
		t = requests.get("https://api.worktile.com/v1/projects", parmas={"access_token": token})
		if 'error_code' in t.text:
			raise ValueError
		else:
			return json.dump(t.text)

	def getProjectDetail(self, pid, token):
		t = requests.get("https://api.worktile.com/v1/projects/" + pid, headers={"access_token": token})
		if "error_code" in t.text:
			raise ValueError
		else:
			return json.dumps(t.text)

	def getProjectMember(self, pid, token):
		t = requests.get("https://api.worktile.com/v1/projects/" + pid + "/members", headers={"access_token": token})
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

	def delpRrojectMember(self, pid, uid, token):
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
		t = requests.get("https://api.worktile.com/v1/entries", data=data)
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
		t = requests.get("https://api.worktile.com/v1/tasks", data=data)
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
