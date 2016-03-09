from GoingMerry.BaseHandler import BaseHandler
from GoingMerry.creat_db import Article, TYPE_ENUM

class AboutHandler(BaseHandler):
	def get(self):
		return self.render2('/about.html', page_title='About me', **self.settings)

class ErrorHandler(BaseHandler):
	def get(self, fuck):
		return self.redirect('/error')

class NotFoundHandler(BaseHandler):
	def get(self):
		return self.render2('404.html', page_title='404', **self.settings)

class FeedHandler(BaseHandler):
	def get(self):
		articles = self.get_database.query(Article).filter(Article.type == TYPE_ENUM[0]).order_by(\
			Article.id.desc()).limit(10).all()
		self.set_header('Content-Type', 'application/xml')
		return self.render2('feed.xml', articles=articles, url=self.get_host(self.request.full_url()),\
		 **self.settings)

	def get_host(self, url):
		return url.split('/')[2]