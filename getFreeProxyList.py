#!/usr/bin/env python

import sys
import urllib2
# from bs4 import BeautifulSoup

def getIpList():
	url = 'http://api.xicidaili.com/free2016.txt'
	try:
		data = urllib2.urlopen(url, timeout=10).read()
		ip_list = data.split('\r\n')
		return ip_list
	except:
		return []
	
# def getKuaiIpList():
# 	resultArray = []
# 	url = 'http://www.kuaidaili.com/free/outha'
# 	try:
# 		response = urllib2.urlopen(url, timeout=10).read()

# 		soup = BeautifulSoup(response, "html.parser")
# 		tbody = soup.find('tbody')
# 		for tag in tbody.find_all('tr'):
# 			ip = tag.find(attrs={"data-title": "IP"}).text
# 			port = tag.find(attrs={"data-title": "PORT"}).text
# 			resultArray.append(ip + ':' + port)
# 	except:
# 		pass
# 	return resultArray

 
if __name__=='__main__':
	reload(sys)
	sys.setdefaultencoding("utf-8")
	print getIpList()