#!/usr/bin/env python

import requests

class wechall(object):
    """
    A class to parse scores out of wechall
    """
    def __init__(self, username):
        self.username = username
        self.baseurl = 'http://www.wechall.net/wechall.php?username=!sites '
        self.challs = []

    def getall(self):
        req = requests.get(self.baseurl+self.username)
        resp = req.content.split(' ')
        index = int(resp.index('primary:'))+1
        allchalls = resp[index:]
        for i in range(0, len(allchalls)):
            self.challs.append(allchalls[i][:-1])
        return self.challs

    def challper(self):
        challdic = {}
        for i in self.challs:
            perc = i.split('(')[1].split(')')[0]
            name = i.split('(')[0]
            challdic[name] = perc
        return challdic
