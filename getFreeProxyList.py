#!/usr/bin/env python

import sys
import urllib2
import requests
from bs4 import BeautifulSoup

def getIpList():
	url = 'http://api.xicidaili.com/free2016.txt'
	data = requests.get(url)
	data = data.text
	ip_list = data.split('\r\n')
	return ip_list
	
def getKuaiIpList():
	resultArray = []
	url = 'http://www.kuaidaili.com/free/outha'
	response = urllib2.urlopen(url).read()

	soup = BeautifulSoup(response, "html.parser")
	tbody = soup.find('tbody')
	for tag in tbody.find_all('tr'):
		ip = tag.find(attrs={"data-title": "IP"}).text
		port = tag.find(attrs={"data-title": "PORT"}).text
		resultArray.append(ip + ':' + port)
	return resultArray

 
if __name__=='__main__':
	reload(sys)
	sys.setdefaultencoding("utf-8")
	print getKuaiIpList()