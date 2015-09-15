#!/usr/bin/python

'''
	This script use for check sites load properly
'''


import urllib2
#someurl means your monitering URLS
someurl = ('http://kasunmadura.com/index.php','http://kasunmadura.com/sample-page/aboutme/')
#match means content which you want to verfy 

match = '136911316406581','http://kasunmadura.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.2.1'

for (i,j) in zip(someurl,match):
	f = urllib2.urlopen(i)	
	print i
	if j in f.read():
        	print 'Site works properly'
		print "#########################################"
	else:		
		print 'Site Not load  issue'
		print "#########################################"





