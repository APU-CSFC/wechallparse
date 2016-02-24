#!/usr/bin/env python
"""
This script provides the main interface to the WeChall API.
"""

import requests

USERURL = 'http://www.wechall.net/wechall.php'
BASEURL = 'http://www.wechall.net/index.php'
BASE_PAYLOAD = {'mo': 'WeChall', 'me': '', 'no_session': '1'}


def userstat(username, sites=False, sitealias=None):
    """
    Query the general user ranking on wechall.
    Query the overview of all sites the user is linked to.
    Query the overview of one particular site the user is playing.
    """
    if sites is False and sitealias is None:
        payload = {'username': username}
    elif sites is True and sitealias is None:
        payload = {'username': '!sites '+username}
    else:
        data = '!'+sitealias+' '+username
        payload = {'username': data}
    req = requests.get(USERURL, params=payload)
    resp = req.content
    return resp


def activity(datestamp=None, username=None, sitename=None, limit=None,
             masterkey=None):
    """"
    Query the latest activity in a machine readable format.
    There are several input parameters for this script
    - datestamp [YYYYmmddhhiiss]: fetch only messages >= this datestamp.
    - username [WeChall Username]: fetch only messages for one user.
    - sitename [Site-name/classname]: fetch only messages for one site.
    - limit [max results]: Limit the results to a value.
    - masterkey [NoLimit]: Raise the max limit of output rows.
    - password [No Api Override for user]: Private API password, when a single
      user is queried.
    """
    payload = BASE_PAYLOAD
    payload['me'] = 'API_History'
    if datestamp is not None:
        payload['datestamp'] = datestamp
    if username is not None:
        payload['username'] = username
    if sitename is not None:
        payload['sitename'] = sitename
    if limit is not None:
        payload['limit'] = limit
    if masterkey is not None:
        payload['masterkey'] = masterkey
    req = requests.get(BASEURL, params=payload)
    resp = req.content
    return resp


def userapi(username, apikey=None):
    """
    Query the UserAPI to get information about a user in machine readble format
    If you submit your private API password, the result will also include your
    newlinks-counter, unreadpm-counter and unreadthreads-counter.
    The output format is multiple rows in key:value pairs.
    """
    payload = BASE_PAYLOAD
    payload['me'] = 'API_User'
    if apikey is None:
        payload['username'] = username
    else:
        payload['username'] = username
        payload['apikey'] = apikey
    req = requests.get(BASEURL, params=payload)
    resp = req.content
    return resp


def siteapi(sitename=None):
    """
    Query the site database with this API to retrieve data in a machine
    readable format.
    """
    payload = BASE_PAYLOAD
    payload['me'] = 'API_Site'
    if sitename is not None:
        payload['sitename'] = sitename
    req = requests.get(BASEURL, params=payload)
    resp = req.content
    return resp
