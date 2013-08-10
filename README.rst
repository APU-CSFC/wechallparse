wechallparse
==============
A class to parse wechall_ challenge percentage for a username.

.. _wechall: http://www.wechall.net/index.php?mo=WeChall&me=JoinUs&section=wechall_api

::

    from wechall import wechall
    
    challs = wechall.challper('mavjs')

    print type(challs)

    >>> <type 'dict'>

    print challs.keys()

    >>> ['WC', 'HTS', 'OTW']

    challs['WC']

    >>> {'percentage': '3.12%', 'name': u'WeChall'}
