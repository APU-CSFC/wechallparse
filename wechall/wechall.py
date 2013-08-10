#!/usr/bin/env python

import os
import requests
import json

baseurl = 'http://www.wechall.net/wechall.php?username=!sites '

def __getall(username):
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
    challnames = os.path.join(os.path.dirname(__file__), 'challnames.json')
    f = open(challnames, 'rb').read()
    longchall = json.loads(f)
    for i in __getall(username):
        perc = i.split('(')[1].split(')')[0]
        sname = i.split('(')[0]
        name = longchall[sname]
        challdict[sname] = { 'name' : name, 'percentage' : perc }
    return challdict


