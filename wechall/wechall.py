#!/usr/bin/env python

import requests

userurl = 'http://www.wechall.net/wechall.php'
baseurl = 'http://www.wechall.net/index.php'
basepayload = {'mo': 'WeChall', 'me': '',
                'no_session': '1'}

def userstat(username, sites=False, sitealias=None):
    if sites is False and sitealias is None:
        payload = {'username': username}
    elif sites is True and sitealias is None:
        payload = {'username': '!sites '+username}
    else:
        data = '!'+sitealias+' '+username
        payload = {'username': data}
    req = requests.get(userurl, params=payload)
    resp = req.content
    return resp

def activity(datestamp=None, username=None, sitename=None, limit=None,
        masterkey=None):
    """"
    Poll the latest activity in a machine readable format.
    """
    if (datestamp,username,sitename,limit,masterkey) is None:
        payload = basepayload
        payload['me'] = 'API_History'
    if not datestamp is None:
        payload['datestamp'] = datestamp
    if not username is None:
        payload['username'] = username
    if not sitename is None:
        payload['sitename'] = sitename
    if not limit is None:
        payload['limit'] = limit
    if not masterkey is None:
        payload['masterkey'] = masterkey
    req = requests.get(baseurl, params=payload)
    resp = req.content
    return resp

def userapi(username, apikey=None):
    payload = basepayload
    payload['me'] = 'API_User'
    if apikey is None:
        payload['username'] = username
    else:
        payload['username'] = username
        payload['apikey'] = apikey
    req = requests.get(baseurl, params=payload)
    resp = req.content
    return resp

def siteapi(sitename=None):
    payload = basepayload
    payload['me'] = 'API_Site'
    if not sitename is None:
        payload['sitename'] = sitename
    req = requests.get(baseurl, params=payload)
    resp = req.content
    return resp
