#!/usr/bin/env python

import sys
import urllib2
import json

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

def getSsList(isProxy, proxyIp=''):
#	url = "https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess"
	url = "http://api.jiasu.im/api/apiv2.php?op=tourist"

	try:
		if isProxy:
			proxy_handler = urllib2.ProxyHandler({'http': proxyIp})
		else:
			proxy_handler = urllib2.ProxyHandler({})

		opener = urllib2.build_opener(proxy_handler)
		urllib2.install_opener(opener)

		# print('proxy ip : ' + proxyIp)
		# response = urllib2.urlopen('http://httpbin.org/ip', timeout=5)
		# return 'original ip : ' + json.loads(response.read())['origin']
		
		req = urllib2.Request(url)
		response = urllib2.urlopen(req, timeout=5).read()
		result = json.loads(response)
		return convertFormat(result)
	except:
		pass

	return ''

def getGimmeIpList():
    url = 'http://gimmeproxy.com/api/getProxy?protocol=http&get=true'

    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request, timeout=5).read()
        result = json.loads(response)
        return result['ip'] + ':' + result['port']
    except:
        pass

    return False

def getFreeSsInfos():
	for i in xrange(0, 20):
		proxyIp = getGimmeIpList()
		if proxyIp == False:
			continue
		
		data = getSsList(isProxy=True, proxyIp=proxyIp)
		if data != '':
			return data
		else:
			continue

	return getSsList(isProxy=False)

if __name__=='__main__':
	reload(sys)
	sys.setdefaultencoding("utf-8")
	print(getFreeSsInfos())