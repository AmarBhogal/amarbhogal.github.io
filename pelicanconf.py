#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Amardeep Bhogal'
SITENAME = 'Amardeep Bhogal'
#SITEURL = 'https://amarbhogal.github.io'
#ABSOLUTE_URL = 'SITEURL'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Contact
LINKS = (('',''),
         ('', ''),
         ('', ''),
         )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/AmarBhogal'),
        ('LinkedIn', 'https://www.linkedin.com/in/amardeep-bhogal/'),)

DEFAULT_PAGINATION = 5

# Theme
THEME='pelican-blueidea'
STATIC_PATHS = ['images', 'static']
FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'static/custom.css'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
