# -*- coding: utf-8 -*- 

import os

namefile=open('sh_stock_name_code','r')
namecodedict={}
while True:
	namecode=namefile.readline().strip()
	if namecode=='' :
		break;
	sps=namecode.split('\t')
	namecodedict[sps[1]]=sps[0]
namefile.close()

files=os.listdir('detail')
filewriter=open('sh_stock_merge','w')
for file in files:
	code=file[3:file.find('.')]
        name=namecodedict[code]
	filereader=open('detail/'+file,'r')
	while True :
		line=filereader.readline().strip()
		if line=='':
			break
		filewriter.write(name+','+code+','+line+'\n')
	filereader.close()	

filewriter.close()
		
