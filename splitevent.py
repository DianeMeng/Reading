#!~/lib/python/bin/python2.7 python
#coding=utf-8
import sys
import re
f=open( sys.argv[1]).readlines()


# pattern = re.compile(r'(.*\|[0-9]+.*)|(.*\|[a-z0-9]{40}.*)')
# pattern = re.compile(r'(.*\|[0-9]+.*)|(.*\|[a-z]{40}.*)')
pattern = re.compile(r'(.*\|[0-9]+.*)|(.*\|[a-z0-9]{40}.*)')
outputs=''
for i  in f:
    id,timeId,time,event,value= i.strip('\n').split(';',4)
    match = pattern.match(event)

    if match is not None :
        # print event
        # print event.split(pattern)
        # print pattern.split(event)
        # print pattern.split(0,event)
        topEvent,secondEvent,leftInfo=event.split('|',2)
        result='|'.join([topEvent,secondEvent])+';'+leftInfo
        # print result
        #out = ';'.join([id,timeId,time,result])+','+value
        out = ';'.join([time,result])+','+value
        outputs+= out+'\\n'
    else:
        out = ';'.join([time,event,value])
        outputs+= out+'\\n'
outputs=outputs.rstrip('\\n')
print outputs
