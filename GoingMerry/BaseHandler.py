import os
import tornado.web
from jinja2 import Environment, FileSystemLoader, ChoiceLoader, TemplateNotFound

from database import db
from filters import *

admin_path = os.path.join(os.path.dirname(__file__), 'themes', 'admin')
admin_template_path = os.path.join(admin_path, 'template')
admin_static_path = os.path.join(admin_path, 'static')

class Jinja2Template(object):
    '''
    A simple class that provides Jinja2's render method
    '''
    def _render(self, path, template_name, **kwargs):
        loader = ChoiceLoader([
                FileSystemLoader(path),
                FileSystemLoader(admin_template_path)
            ])
        env = Environment(loader=loader)
        env.filters['datetime'] = datetime
        env.filters['markdown'] = markdown

        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
    	return template.render(kwargs)

class BaseHandler(tornado.web.RequestHandler, Jinja2Template):
    @property
    def get_database(self):
        return db()    
    def unconnect_database(self):
        return self.get_database.close()

    def render2(self, template_name, **kwargs):
        self.set_header('X-Powered-By', 'ThousandSunny')
        self.write(self._render(self.settings['template_path'], template_name, **kwargs))

    '''Override get_current_user()'''
    def get_current_user(self):
        return self.get_secure_cookie('username')