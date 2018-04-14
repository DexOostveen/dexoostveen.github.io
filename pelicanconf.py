#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dex Oostveen'
SITENAME = 'Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        # ('github','https://github.com/DexOostveen')
        # ('Pelican', 'http://getpelican.com/'),
        #  ('Python.org', 'http://python.org/'),
        #  ('Jinja2', 'http://jinja.pocoo.org/'),
        #  ('You can modify those links in your config file', '#')
         
         )
# GITHUB_URL = 'https://github.com/DexOostveen'

# Social widget
SOCIAL = (
        ('github','https://github.com/DexOostveen')
        # ('You can add links in your config file', '#'),
#           ('Another social link', '#')
       ,)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-blueidea'
### pelican-blueidea
DISPLAY_CATEGORIES_ON_SUBMENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_SEARCH_FORM =False