from __future__ import division
from math import ceil

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import func, and_

from GoingMerry.creat_db import Article, TYPE_ENUM
from GoingMerry.BaseHandler import BaseHandler
from GoingMerry.settings import SHOW_ARTICLE_NUM

class ListArticleHandler(BaseHandler):
	def get(self, page=1):
		page = int(self.get_argument('page', 1))
		count = self.get_database.query(func.count('*')).filter(Article.type == TYPE_ENUM[0]).scalar()
		pages = int(ceil(count / SHOW_ARTICLE_NUM))
		if page < 1 or page > pages:
			return self.render2('articles.html', page_title='Article', articles=[], index=[], \
								**self.settings)
		try:
			articles = self.get_database.query(Article.title, Article.creat_time).filter(Article.type\
				== TYPE_ENUM[0]).order_by(Article.id.desc()).limit(SHOW_ARTICLE_NUM).offset((page - 1) *\
				SHOW_ARTICLE_NUM).all()
			pages = range(1, pages + 1)
			if len(pages) < 2:
				pages = False
		except NoResultFound:
			self.redirect('/error')
		return self.render2('articles.html', page_title='Article', articles=articles, index=dict(
				older = page - 1,
				newer = page + 1,
				now = page,
				pages = pages,
			), **self.settings)

class ListEssayHandler(BaseHandler):
	def get(self, page=1):
		page = int(self.get_argument('page', 1))
		count = self.get_database.query(func.count('*')).filter(Article.type == TYPE_ENUM[1]).scalar()
		pages = int(ceil(count / SHOW_ARTICLE_NUM))
		if page < 1 or page > pages:
			return self.render2('essay.html', page_title='Essay', articles=[], index=[], \
								**self.settings)
		try:
			articles = self.get_database.query(Article.title, Article.creat_time).filter(Article.type\
				== TYPE_ENUM[1]).order_by(Article.id.desc()).limit(SHOW_ARTICLE_NUM).offset((page - 1)\
				 * SHOW_ARTICLE_NUM).all()
			pages = range(1, pages + 1)
			if len(pages) < 2:
				pages = False
		except NoResultFound:
			self.redirect('/error')
		return self.render2('essay.html', page_title='Essay', articles=articles, index=dict(
				older = page - 1,
				newer = page + 1,
				now = page,
				pages = pages,
			), **self.settings)
class ShowArticleHandler(BaseHandler):
	def get(self, title):
		try:
			articles = self.get_database.query(Article).filter(and_(Article.title == title, Article.type\
				== TYPE_ENUM[0])).one()
			title_id, = self.get_database.query(Article.id).filter(and_(Article.title == title, \
					Article.type == TYPE_ENUM[0])).one()
			try:
				all_title = self.get_database.query(Article.id, Article.title).filter(Article.type\
				 == TYPE_ENUM[0]).order_by(Article.id.desc()).all()
				for i in all_title:
					if title_id in i:
						title_index = all_title.index(i)
			except ValueError:
				older_title = False
				newer_title = False

			if title_index == 0:
				newer_title = False
				older_title = all_title[title_index + 1].title
			elif title_index == len(all_title) - 1:
				newer_title = all_title[title_index - 1].title
				older_title = False
			else:
				older_title = all_title[title_index + 1].title
				newer_title = all_title[title_index - 1].title
			
		except NoResultFound:
			self.redirect('/error')
		return self.render2('show_article.html', page_title=title, articles=articles, pages=dict(
				type = 'article',
				older_title = older_title,
				newer_title = newer_title,
			), **self.settings)

class ShowEssayHandler(BaseHandler):
	def get(self, title):
		try:
			articles = self.get_database.query(Article).filter(and_(Article.title == title, Article.type\
				== TYPE_ENUM[1])).one()
			title_id, = self.get_database.query(Article.id).filter(and_(Article.title == title, \
					Article.type == TYPE_ENUM[1])).one()
			try:
				all_title = self.get_database.query(Article.id, Article.title).filter(Article.type\
				 == TYPE_ENUM[1]).order_by(Article.id.desc()).all()
				for i in all_title:
					if title_id in i:
						title_index = all_title.index(i)
			except ValueError:
				older_title = False
				newer_title = False

			if title_index == 0:
				newer_title = False
				older_title = all_title[title_index + 1].title
			elif title_index == len(all_title) - 1:
				newer_title = all_title[title_index - 1].title
				older_title = False
			else:
				older_title = all_title[title_index + 1].title
				newer_title = all_title[title_index - 1].title
		except NoResultFound:
			self.redirect('/error')
		return self.render2('show_article.html', page_title=title, articles=articles, pages=dict(
				type = 'essay',
				older_title = older_title,
				newer_title = newer_title,
			), **self.settings)
