#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


### Site Setting
AUTHOR = 'CHANN'
SITENAME = 'CHANN Wiki'
SITESUBTITLE = 'Github-based Wiki'
SITEURL = 'http://wiki.chann.kr'
# SITEURL = 'http://localhost:8000'
DISQUS_SITENAME = u'chann-wiki'
# DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
# DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'
# GOOGLE_ANALYTICS = ""
# GITHUB_USER = 'channprj'


### Theme Setting
THEME = 'theme/peliwiki'
# THEME = 'theme/replika'

DIRECT_TEMPLATES = ('index', 'search', 'archives', 'categories','tags','page_list')
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
HIDE_SIDEBAR = True
MENUITEMS = (
    ('인덱스', '/indexed'),
    ('최근문서', '/recent'),
    ('언어', '/languages'),
    ('랭킹', '/rank'),
)

### Plugin Setting
PLUGIN_PATHS = ['plugin']
PLUGINS = ['always_modified','related_posts','interlinks','pelican-page-hierarchy']  # 'random_article'

ALWAYS_MODIFIED = True
RELATED_POSTS_MAX = 5
# RANDOM = 'random.html'
INTERLINKS = {
    '메인': 'http://wiki.chann.kr',
    'travis-ci': 'http://wiki.chann.kr/travis-ci'
}
SLUGIFY_SOURCE = 'basename'


# Build Setting
OUTPUT_PATH = 'output'
PATH = 'content'
TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'ko'


### Feed Setting
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (
         ('Blog', 'http://blog.chann.kr'),
)


# Social
SOCIAL = (
	('Resume', 'https://chann.kr'),
	('Github', 'https://github.com/channprj'),
	('Twitter', 'https://twitter.com/chann_kr'),
	('Facebook', 'https://fb.com/channprj'),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


### Remove html extension
ARCHIVE_URL = '{archive}'
ARCHIVE_SAVE_AS = ARCHIVE_URL+'.html'

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL+'.html'

PAGE_URL = '{slug}'
# PAGE_SAVE_AS = PAGE_URL+'.html'
PAGE_SAVE_AS = PAGE_URL+'/index.html'  # Multi Page

CATEGORY_URL = '{slug}/index'
CATEGORY_SAVE_AS = CATEGORY_URL+'.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = TAG_URL+'.html'

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = AUTHOR_URL+'.html'
