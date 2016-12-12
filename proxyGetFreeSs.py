#!/usr/bin/env python

import os
import sys
import urllib2
import json

from getFreeProxyList import *

def convertFormat(json):
	hjson = json['msg']['ss']
	data = ''
	for i in xrange(0, len(hjson)):
		data += hjson[i]['serverip']
		data += ' ' 
		data += hjson[i]['port']
		data += ' '
		data += hjson[i]['authscheme']
		data += ' '
		data += hjson[i]['passwd']
		data += ' '
		data += hjson[i]['servername']
		data += '\n'
	return data

def getFreeSsInfos():
#	url = "https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess"
	url = "http://api.jiasu.im/api/apiv2.php?op=tourist"	

	proxyIpList = getXiciIpList()
	# proxyIpList = getKuaiIpList()

	for proxyIp in proxyIpList:
		try:
			proxy_handler = urllib2.ProxyHandler({'http': proxyIp})
			opener = urllib2.build_opener(proxy_handler)
			urllib2.install_opener(opener)

			# print('proxy ip : ' + proxyIp)
			# response = urllib2.urlopen('http://httpbin.org/ip', timeout=3)
			# print('original ip : ' + json.loads(response.read())['origin'])
			# continue
			
			response = urllib2.urlopen(url, timeout=3)
			result = json.loads(response.read())
			return convertFormat(result)
			break
		except:
			pass
	try:
		proxy_handler = urllib2.ProxyHandler({})
		opener = urllib2.build_opener(proxy_handler)
		urllib2.install_opener(opener)

		# response = urllib2.urlopen('http://httpbin.org/ip', timeout=5)
		# print('original ip : ' + json.loads(response.read())['origin'])
		# return ''

		response = urllib2.urlopen(url, timeout=5)
		result = json.loads(response.read())
		return convertFormat(result)
	except:
		pass

	return ''

if __name__=='__main__':
	reload(sys)
	sys.setdefaultencoding("utf-8")
	print(getFreeSsInfos())