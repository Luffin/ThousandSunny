import os

# You can name your own database's name
DB_FILENAME = 'luffin'
CUR_DIR = os.path.abspath('.')
DB_DIR = "sqlite:///%s" % (os.path.join(CUR_DIR, '{}.db'.format(DB_FILENAME)))

# cookie_secret must be set and keep it secret
COOKIE_SECRET = '6V9btAYiTnCQOS+L+NQOPgUvTqLOoExepMxzBF0OdTI='

# You can choose theme by setting theme_name
theme_name = 'jekyll-minimal-theme-gh-pages'

# Blog's title
title = "Luffin's Blog"

# Email
email = 'luffin@qq.com'

# How many articles do you want to display in home page
ARTICLES_NUM = 3

# How many articles do you want to dispay in the article/essay page
SHOW_ARTICLE_NUM = 15