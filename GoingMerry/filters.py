import re
from markdown import markdown as md

def datetime(value, format='%b %d, %Y'):
	return value.strftime(format)

def markdown(content):
	return a_blank(md(content))

def a_blank(content):
	'''Replace <a href="##"> to <a href="##" target="_blank">'''
	return re.sub(r'<a href="(.+?">)', lambda m: '{}" target="_blank">'.\
			format(m.group(0)[:-2]), content)