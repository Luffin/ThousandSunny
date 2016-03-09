from datetime import date
from hashlib import md5

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text, Enum

from database import engine

ARTICLE = 'article'
ESSAY = 'essay'
TYPE_ENUM = (ARTICLE, ESSAY)

Base = declarative_base();

class Article(Base):
	__tablename__ = 'articles'

	id = Column(Integer, primary_key=True)
	title = Column(String(200), nullable=False, unique=True)
	content = Column(Text)
	type = Column(Enum(*TYPE_ENUM), default=ARTICLE)
	creat_time = Column(Date, default=date.today())

	def __repr__(self):
		return "<Article(id='%d', title='%s')>" % (
			self.id, self.title)

class Friend(Base):
	__tablename__ = 'friends'

	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	url = Column(String(100))

	def __repr__(self):
		return "<Friend(id='%d', name='%s', url='%s')>" % (
			self.id, self.name, self.url)

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	username = Column(String(20))
	password = Column(String(32))

	def checkPassword(self, password):
		return self.password == md5(password).hexdigest()

	def __repr__(self):
		return "<User(id='%d', username='%s', password='%s')>" % (
		 	self.id, self.username, self.password)

if __name__ == '__main__':
	Base.metadata.create_all(engine)