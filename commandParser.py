__author__ = 'broncotc'


def commandParser(command):
	temp = command.replace("@worktile_bot", "")
	return temp


def Central_txt(start_str, end, html):
	start = html.find(start_str)
	if start >= 0:
		start += len(start_str)
		end = html.find(end, start)
		if end >= 0:
			return html[start:end].strip()
