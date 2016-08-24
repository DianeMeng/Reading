#!~/lib/python/bin/python2.7 python
#coding=utf-8
from collections import Counter
from collections import Counter as mset
import sys
f=open( sys.argv[1]).readlines()

ids=[]
timeIds=[]
times=[]
events=[]
timeList=[]
valueList=[]
cpvalueList=[]
for i in f:
    # print i.strip('\n')
    id,timeId,time,event,value= i.strip('\n').split(';')
    ids.append(str(id))
    timeIds.append(str(timeId))
    times.append(time)
    events.append(event)
    timeList.append(time)
    valueList.append(value)
    cpvalueList.append(value)

# firstrow=(ids[0],timeId[0],time)
def handle():
    if len(valueList)==0:
        return 
    del valueList[-1]
    del cpvalueList[0]

    firstCount=None
    states=[]
    states.append('count:'+str(len(valueList[0].split(','))))
    for i,v in enumerate(valueList):
        state=None
        v = v.split(',')
        cpv = cpvalueList[i]
        cpv = cpv.split(',')
    # if set(v)!=set(cpv):
    #     if len(v)==len(cpv):
    #         state = 'add and del'
    #         dels=set(v)-set(cpv)
    #         adds=set(cpv)-set(v)
    #         print len(dels)
    #         # print len(adds)
    #     elif len(v)< len(cpv):
    #         if set(v).issubset(set(cpv)):
    #             state = 'add'
    #         else :
    #             state ='add and del'
    #     else:
    #         if set(cpv).issubset(set(v)):
    #             state ='del'
    #         else:
    #             state= 'add and del'

        dels=mset(v)-mset(cpv)
        adds=mset(cpv)-mset(v)
        delssize=len(list(dels.elements()))
        addssize=len(list(adds.elements()))
        state = 'count:'+str(len(cpv))
        if delssize == 0 and addssize==0:
            1==1
        elif delssize != 0 and addssize ==0:
            state +='.del:'+str(delssize)
        elif delssize ==0 and addssize !=0:
            state += '.add:'+str(addssize)
        else :
            state +='.add:'+str(addssize) +' and '+ 'del:'+str(delssize)

        states.append(state)

    finalOut=''
    for i,v in enumerate(ids):
        # print type(states[i])
        #output=';'.join([ids[i],timeIds[i],times[i],events[i],states[i]])
        output=';'.join([times[i],events[i],states[i]])
        # outputs.append(output)
        # print output
        finalOut += output
        if i != len(ids)-1:
            finalOut += '\\n'

    print finalOut
handle()
