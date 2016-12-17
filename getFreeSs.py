#!/usr/bin/env python
#coding:utf-8

import sys
import urllib2
import json

def getFreeSsInfos():
    url = "http://api.jiasu.im/api/apiv2.php?op=tourist"

    try:
        # url = "https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess"
        response = urllib2.urlopen(url, timeout=10)
        result = json.loads(response.read())

        hjson = result['msg']['ss']
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
            if hjson[i]['status'] == '6':
                data += '[不可用]'
            data += hjson[i]['servername']
            data += '\n'
        return data
    except:
        return ''

if __name__=='__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    print(getFreeSsInfos())