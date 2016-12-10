#!/usr/bin/env python

import sys
import urllib2
import json

def getFreeSsInfos():
	url = "https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess"
	response = urllib2.urlopen(url)
	hjson = json.loads(response.read())
	data = ''
	for i in xrange(0, len(hjson)):
		data += hjson[i]['i'] + ' ' + hjson[i]['p'] + ' ' + hjson[i]['m'] + ' ' + hjson[i]['pw'] + ' ' + hjson[i]['r']
		data += '\n'
	return data

if __name__=='__main__':
	reload(sys)
	sys.setdefaultencoding("utf-8")
	print(getFreeSsInfos())