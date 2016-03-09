import os

from tornado import web

from settings import *
from handlers import handlers

theme_path = os.path.join(os.path.dirname(__file__), 'themes', theme_name)


class Application(web.Application):
	def __init__(self):
		settings = dict(
			static_path = os.path.join(theme_path, 'static'),
			template_path = os.path.join(theme_path, 'template'),
			debug = True,
			title = title,
			email = email,
			login_url = '/onepeice',
			cookie_secret = '6V8btAYiTnCQOS+L+NQOPgUvTqLOoExepMxzBF0OdTI=',
			)
		super(Application, self).__init__(handlers, **settings)