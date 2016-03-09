from __future__ import division
from math import ceil

from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound

from GoingMerry.BaseHandler import BaseHandler
from GoingMerry.creat_db import Article, TYPE_ENUM
from GoingMerry.settings import ARTICLES_NUM

class IndexHandler(BaseHandler):
	def get(self, page=1):
		page = int(self.get_argument('page', 1))
		count = self.get_database.query(func.count('*')).filter(Article.type == TYPE_ENUM[0]).scalar()
		pages = int(ceil(count / ARTICLES_NUM))
		if page < 1 or page > pages:
			return self.render2('index.html', page_title='Welcome', articles=[], index=[], \
								**self.settings)
		try:
			articles = self.get_database.query(Article).filter(Article.type == TYPE_ENUM[0]).order_by(\
				Article.id.desc()).limit(ARTICLES_NUM).offset((page -1) * ARTICLES_NUM).all()
			pages = range(1, pages + 1)
			if len(pages) < 2:
				pages = False
		except NoResultFound:
			self.redirect('/error')
		return self.render2('index.html', page_title='Welcome', articles=articles,\
						index=dict(
							older = page - 1,
							newer = page + 1,
							now = page,
							pages = pages,
						), **self.settings)