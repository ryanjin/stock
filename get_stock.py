# -*- coding: utf-8 -*- 
import httplib
import time
import urllib

url="table.finance.yahoo.com"
path="/table.csv?s="
file = open('sh_stock_code')


for i in range(1023):
	file.readline()

while True:
	code=file.readline().strip()
	print code
	if code=='':
		break;
	
	geturl=path+code+'.ss'
	conn=httplib.HTTPConnection(url)
	conn.request("GET",geturl)
	ret=conn.getresponse()
	if ret.status != 200:
		print code,'not success',geturl,ret.status
		continue
	detail=ret.read()
	conn.close()
	filewrite=open('detail/sh_'+code+'.csv','w')
	filewrite.write(detail)
	filewrite.flush()
	filewrite.close()
	
	time.sleep(0.01)

file.close()
	
