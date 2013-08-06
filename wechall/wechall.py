#!/usr/bin/env python

import requests

baseurl = 'http://www.wechall.net/wechall.php?username=!sites '

def getall(username):
    challs = []
    req = requests.get(baseurl+username)
    resp = req.content.split(' ')
    index = int(resp.index('primary:'))+1
    allchalls = resp[index:]
    for i in range(0, len(allchalls)):
        challs.append(allchalls[i][:-1])
    return challs

def challper(username):
    challdict = {}
    for i in getall(username):
        perc = i.split('(')[1].split(')')[0]
        name = i.split('(')[0]
        challdict[name] = perc
    return challdict
