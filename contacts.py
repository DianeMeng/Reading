#!~/lib/python/bin/python2.7 python
#coding=utf-8

from collections import Counter
from collections import Counter as mset

import sys
f=open( sys.argv[1]).readlines()

valueList=[]
outputs=''
for i in f:
    # print i.strip('\n')
    id,timeId,time,event,value= i.strip('\n').split(';',4)
    # print value
    person=mset(value.split(';'))
    listperson=list(person.elements())
    calls=len(listperson)#count
    # for p in listperson:
    #     print p
    # print calls
    # print '-------'
    nonecnc=0
    onecnc=0
    twocnc=0
    threecnc=0
    threemorecnc=0
    emails=0
    photos=0
    for k,v in  person.items():
        # print k
        # print v
        call,email,photo,status=k.split(',')
        # calls.append(call)
        call =int(call)
        if call==0:
            nonecnc+=v
        elif call == 1:
            onecnc+=v
        elif call == 2:
            twocnc+=v
        elif call == 3:
            threecnc+=v
        else:
            threemorecnc+=v
        emails+=int(email)*v
        if photo == 'true':
            photos+=v
    result=','.join([str(calls),str(nonecnc),str(twocnc),str(threecnc),str(threemorecnc),str(emails),str(photos)])
    #output=';'.join([id,timeId,time,event,result])
    output=';'.join([time,event,result])
    outputs+=output+'\\n'

outputs=outputs.rstrip('\\n')
print outputs

