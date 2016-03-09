from GoingMerry.BaseHandler import admin_static_path

from tornado.web import StaticFileHandler
from IndexHandler import IndexHandler
from AdminHandler import SighInHandler, AddArticleHandler, ManageArticleHandler, ManageFriendHandler
from PostHandler import ListArticleHandler, ListEssayHandler, ShowArticleHandler, ShowEssayHandler
from FriendHandler import FriendHandler
from OtherHandler import AboutHandler, NotFoundHandler, ErrorHandler, FeedHandler

handlers = [
	# index
	(r'/', IndexHandler),

	#feed.xml
	(r'/feed', FeedHandler),

	# about
	(r'/about', AboutHandler),

	# admin
	(r'/onepeice', SighInHandler),
	(r'/onepeice/article', ManageArticleHandler),
	(r'/onepeice/friend', ManageFriendHandler),
	(r'/onepeice/post/article', AddArticleHandler),
	(r'/admin/static/(.*)', StaticFileHandler, dict(path = admin_static_path)),

	# articles
	(r'/article', ListArticleHandler),
	(r'/article/(.*)', ShowArticleHandler),

	# essay
	(r'/essay', ListEssayHandler),
	(r'/essay/(.*)', ShowEssayHandler),

	# friends
	(r'/friends', FriendHandler),

	# 404
	(r'/error', NotFoundHandler),
	(r'/(.*)', ErrorHandler),

]