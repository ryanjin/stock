# -*- coding: utf-8 -*- 

import sys

file = sys.argv[1]
fileReader = open(file,'r')
fileWriter = open(file+'_processed','w')

spt=fileReader.readline().split(' ')
print len(spt)
for string in spt :
	i1=string.find('(')
	i2=string.find(')')
	name=string[0:i1]
	code=string[i1+1:i2]
	fileWriter.write(code+'\n')

fileReader.close()
fileWriter.close()

