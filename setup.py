#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='wechall',
    packages=['wechall'],
    version='0.2',
    description='wechall score parser',
    long_description=open('README.rst').read() + '\n',
    author='Maverick JS',
    author_email='mavjs01@gmail.com',
    url='https://github.com/APU-CSFC/wechallparse',
    download_url='https://github.com/APU-CSFC/wechallparse/archive/master.tar.gz',
    package_data={'': ['LICENSE'], 'wechall': ['*.json']},
    package_dir={'wechall' : 'wechall'},
    include_package_data=True,
    install_requires=['requests'],
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ),
)
