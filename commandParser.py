# TODO: remove "@worktile_bot" if exist
__author__ = 'broncotc'
import re
def commandParser(command):
	print command
	temp = command.replace("@worktile_bot","")
	return temp

def MessageParser(code):
	if code[0] == " ":
		code = code[1:]
	temp = Central_txt("/"," ",code)
	if temp == "image":
		pass
	elif temp == "bot":
		pass
	elif temp == "text":
		pass
def Central_txt(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()
MessageParser(" /bot /title textmessagebox")