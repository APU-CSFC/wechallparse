#!/usr/bin/env python
"""This is the WeChall API test suite."""

from nose.tools import assert_equal
import wechall

def test_userstat_general():
    """Get general status of user on WeChall."""
    userstatreq = wechall.userstat("mavjs")
    reqstat = b"""mavjs is ranked 2377 from 13723, linked to 5 sites with an
            average of 9.21% solved. mavjs has a totalscore of 3096. mavjs
            needs 3 points to rankup."""
    assert_equal(userstatreq, reqstat)

def test_userstat_overviewsites():
    """Get general status of user on each wargame site."""
    userstatreq = wechall.userstat("mavjs", True)
    reqstat = b"""mavjs plays 5 sites, primary: OTW(25.62%), NF(9.57%),
            HTS(6.72%), WC(2.76%), EG(1.36%)."""
    assert_equal(userstatreq, reqstat)

def test_userstat_overviewsite():
    """Get status of user on a particular wargame site."""
    userstatreq = wechall.userstat("mavjs", True, "OTW")
    reqstat = b"""mavjs completed %25.62 on OverTheWire.org (41 of 160 points).
            On http://www.overthewire.org/wargames/ , mavjs's rank is unknown.
            Linked to WeChall he claims rank 496, scoring 2735 points."""
    assert_equal(userstatreq, reqstat)
