from GoingMerry.BaseHandler import BaseHandler
from GoingMerry.creat_db import Friend

class FriendHandler(BaseHandler):
	def get(self):
		return self.render2('friends.html', page_title='My Friends', \
			friends=self.get_database.query(Friend).all(), **self.settings)