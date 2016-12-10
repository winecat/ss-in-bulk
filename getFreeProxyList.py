#!/usr/bin/python

import os
import sys
import urllib2
import json
import socket
import requests

def getIpList():
	url = 'http://api.xicidaili.com/free2016.txt'
	data = requests.get(url)
	data = data.text
	ip_list = data.split('\r\n')
	return ip_list

#if __name__=='__main__':
#	reload(sys)
#	sys.setdefaultencoding("utf-8")
#	print(getIpList())