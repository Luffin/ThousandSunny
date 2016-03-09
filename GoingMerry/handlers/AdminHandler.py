import tornado.web

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import func, and_

from GoingMerry.BaseHandler import BaseHandler
from GoingMerry.creat_db import Article, Friend, User, TYPE_ENUM

class SighInHandler(BaseHandler):
	def get(self):
		return self.render2('login.html')

	def post(self):
		username = self.get_argument('user', None)
		password = self.get_argument('pass', None)
		if username and password:
			try:
				user = self.get_database.query(User).filter(User.username == username).one()
			except NoResultFound:
				self.redirect('/onepeice')
			
			if user.checkPassword(password):
				self.set_secure_cookie('username', user.username, expires_days=5)
				return self.redirect('/onepeice/article')
		return self.redirect('/onepeice')


class AddArticleHandler(BaseHandler):
	@tornado.web.authenticated
	def post(self):
		id = int(self.get_argument('id', -1))
		if id > -1:
			new_id = self.get_argument('new_id', None)
			self.write('<script>alert('+str(new_id)+')</script>')
			title = self.get_argument('title', None)
			type = self.get_argument('type', None)
			content = self.get_argument('content', None)
			try:
				self.get_database.query(Article).filter(Article.id == id).\
					update({
							Article.id:new_id,
							Article.title:title,
							Article.type:type,
							Article.content:content
						})
				self.get_database.commit()
				return self.redirect('/onepeice/article')
			except Exception:
				return self.redirect('/onepeice/article')
			
		else:
			self.write('add')
			title = self.get_argument('title', None)
			type = self.get_argument('type', None)
			content = self.get_argument('content', None)
			try:
				query = self.get_database.query(Article).filter(Article.title == title).one()
			except NoResultFound:
				if not title or not type or not content:
					return self.redirect('/onepeice/article')
				self.get_database.add(Article(title=title, content=content, type=type))
				self.get_database.commit()
				return self.redirect('/onepeice/article')
			else:
				return self.redirect('/onepeice/article')

class ManageArticleHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		action = self.get_argument('action', None)
		id = int(self.get_argument('id', -1))
		type = self.get_argument('type', None)
		if action == 'edit' and id > -1 and type:
			article = self.get_database.query(Article).filter(and_(Article.id == id, Article.type == type)).one()
			return self.render2('edit_article.html', article=article)
		else:
			article_count = self.get_database.query(func.count('*')).filter(Article.type == TYPE_ENUM[0])\
							.scalar()
			essay_count = self.get_database.query(func.count('*')).filter(Article.type == TYPE_ENUM[1])\
							.scalar()
			if article_count or essay_count:
				articles = self.get_database.query(Article.id, Article.creat_time, Article.title,\
							 Article.type).filter(Article.type == TYPE_ENUM[0]).all()
				essays = self.get_database.query(Article.id, Article.creat_time, Article.title,\
							 Article.type).filter(Article.type == TYPE_ENUM[1]).all()
				return self.render2('admin_article.html', article_count=article_count+1, \
									essay_count=essay_count+1,articles=articles, essays=essays)
			return self.render2('admin_article.html')

	@tornado.web.authenticated
	def post(self):
		action = self.get_argument('action', None)
		if action == 'del':
			article_id = self.get_argument('id')
			if article_id:
				article = self.get_database.query(Article).filter(Article.id == int(article_id)).one()
				self.get_database.delete(article)
				self.get_database.commit()	

class ManageFriendHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		action = self.get_argument('action', None)
		if action and action == 'edit':
			id = int(self.get_argument('id', -1))
			if id > -1:
				friend = self.get_database.query(Friend).filter(Friend.id == id).one()
				return self.render2('edit_friend.html', friend=friend)
		else:
			friends = self.get_database.query(Friend).all()
			return self.render2('admin_friend.html', friends=friends, **self.settings)

	@tornado.web.authenticated
	def post(self):
		action = self.get_argument('action', None)
		new_id = int(self.get_argument('new_id', -1))
		if action == 'add' and new_id == -1:
			name = self.get_argument('name', None)
			url = self.get_argument('url', None)
			if not name and not url:
				return self.redirect('/onepeice/friend')
			self.get_database.add(Friend(name=name, url=url))
			self.get_database.commit()
			return self.redirect('/onepeice/friend')
		elif action == 'del' and new_id == -1:
			friend_id = self.get_argument('id')
			if friend_id:
				friend = self.get_database.query(Friend).filter(Friend.id == int(friend_id)).one()
				self.get_database.delete(friend)
				self.get_database.commit()
		elif new_id > -1:
			id = int(self.get_argument('id', -1))
			name = self.get_argument('name', None)
			url = self.get_argument('url', None)
			if not name and not url and id < 0:
				return self.redirect('/onepeice/friend')
			try:
				self.get_database.query(Friend).filter(Friend.id == id).update({
					Friend.id:new_id,
					Friend.name:name,
					Friend.url:url
					})
				self.get_database.commit()
				return self.redirect('/onepeice/friend')
			except Exception:
				return self.redirect('/onepeice/friend')


