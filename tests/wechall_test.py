#!/usr/bin/env python

from nose.tools import *
import wechall

def test_UserstatGeneral():
    userstatreq = wechall.userstat("mavjs")
    reqstat = 'mavjs is ranked 2377 from 13723, linked to 5 sites with an average of 9.21% solved. mavjs has a totalscore of 3096. mavjs needs 3 points to rankup.'
    assert_equal(userstatreq, reqstat)

def test_UserstatOverviewSites():
    userstatreq = wechall.userstat("mavjs", True)
    reqstat = 'mavjs plays 5 sites, primary: OTW(25.62%), NF(9.57%), HTS(6.72%), WC(2.76%), EG(1.36%).'
    assert_equal(userstatreq, reqstat)

def test_UserstatOverviewSite():
    userstatreq = wechall.userstat("mavjs", True, "OTW")
    reqstat = "mavjs completed %25.62 on OverTheWire.org (41 of 160 points). On http://www.overthewire.org/wargames/ , mavjs's rank is unknown. Linked to WeChall he claims rank 496, scoring 2735 points."
    assert_equal(userstatreq, reqstat)
