wechallparse
==============
A class to parse wechall_ challenge percentage for a username.

.. _wechall: http://www.wechall.net/index.php?mo=WeChall&me=JoinUs&section=wechall_api

You can install this package by issuing::

    sudo python setup.py install

or::

    su -c "python setup.py install"

Then use the package by doing::

    In [1]: import wechall

    In [2]: wechall.userstat('mavjs')
    Out[2]: 'mavjs is ranked 1605 from 8333, linked to 3 sites with an average of 12.91% solved. mavjs has a totalscore of 3070. mavjs needs 2 points to rankup.'

    In [3]: wechall.userstat('mavjs', True)
    Out[3]: 'mavjs plays 3 sites, primary: OTW(29.08%), HTS(6.72%), WC(2.92%).'

    In [4]: wechall.userstat('mavjs', True, 'OTW')
    Out[4]: "mavjs completed %29.08 on OverTheWire.org (41 of 141 points). On http://www.overthewire.org/wargames/ , mavjs's rank is unknown. Linked to WeChall he claims rank 96, scoring 2910 points."
