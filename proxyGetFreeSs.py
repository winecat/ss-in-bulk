#!/usr/bin/env python

import os
import sys
import urllib2
import json

from getFreeProxyList import *

def getFreeSsInfos():
#	url = "https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess"
	url = "http://api.jiasu.im/api/apiv2.php?op=tourist"	

	data = ''	
	# proxyIpList = getIpList()
	# proxyIpList = getKuaiIpList()
	proxyIpList = []

	for proxyIp in proxyIpList:
		try:
			proxy_handler = urllib2.ProxyHandler({'http': proxyIp})
			opener = urllib2.build_opener(proxy_handler)
			urllib2.install_opener(opener)

			# print('gotten ip : ' + proxyIp)
			# response = urllib2.urlopen('http://httpbin.org/ip', timeout=3)
			# print('origin ip : ' + json.loads(response.read())['origin'])
			# continue
			
			response = urllib2.urlopen(url, timeout=3)
			result = json.loads(response.read())
			hjson = result['msg']['ss']
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
			break
		except:
			pass
	return data

if __name__=='__main__':
	reload(sys)
	sys.setdefaultencoding("utf-8")
	print(getFreeSsInfos())