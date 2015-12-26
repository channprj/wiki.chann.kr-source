#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CHANN'
SITENAME = 'CHANN Wiki'
SITESUBTITLE = 'Personal Wiki'
SITEURL = 'http://wiki.chann.kr'
# SITEURL = 'http://localhost:8000'
DISQUS_SITENAME = u'chann-wiki'
# DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
# DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'
# GOOGLE_ANALYTICS = ""

### THEME SETTING
THEME = 'theme/peliwiki'
# THEME = 'theme/replika'

DIRECT_TEMPLATES = ('index', 'search', 'archives', 'categories','tags',)
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

OUTPUT_PATH = 'output'
PATH = 'content'

TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Blog', 'http://blog.chann.kr'),
)

# Social widget
SOCIAL = (
	('Resume', 'https://chann.kr'),
	('Github', 'https://github.com/channprj'),
	('Twitter', 'https://twitter.com/chann_kr'),
	('Facebook', 'https://fb.com/channprj'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Remove html extension
# ARCHIVE_URL = '{archive}'
# ARCHIVE_SAVE_AS = ARCHIVE_URL+'.html'

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL+'.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = PAGE_URL+'.html'

CATEGORY_URL = '{slug}/index'
CATEGORY_SAVE_AS = CATEGORY_URL+'.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = TAG_URL+'.html'

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = AUTHOR_URL+'.html'
