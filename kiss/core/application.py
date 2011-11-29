from gevent import monkey; monkey.patch_all()
from gevent.wsgi import WSGIServer
from helpers import Singleton, Importer, DictHelper
from kiss.controllers.router import Router
from kiss.views.base import Request, Response
from beaker.middleware import SessionMiddleware
from werkzeug.wsgi import SharedDataMiddleware

class Application(object):
	__metaclass__ = Singleton
	
	def __init__(self, options):
		self.options = {
			"application": {
				"address": "127.0.0.1",
				"port": 8080
			},
			"views": {
				"templates_path": "views.templates",
				"static_path": "views.static",
				'session_type': "cookie",
				"session_auto": True,
				'session_cookie_expires': True,
				'session_encrypt_key':'sldk24j0jf09w0jfg24',
				'session_validate_key':';l[pfghopkqeq1234,fs'
			}
		}
		self.options = DictHelper.merge(self.options, options)
		self.router = Router(self.options)
			
	def wsgi_app(self, options, start_response):
		request = Request(options)
		response = self.router.route(request)
		if not response:
			response = Response("404 Not Found")
		return response(options, start_response)
	
	def start(self):
		session_options = {
			'session.type': self.options["views"]['session_type'],
			"session.auto": self.options["views"]["session_auto"],
			'session.cookie_expires': self.options["views"]['session_cookie_expires'],
			'session.encrypt_key': self.options["views"]['session_encrypt_key'],
			'session.validate_key': self.options["views"]['session_validate_key']
		}
		if "static_path" in self.options["views"]:
			try:
				static_path = Importer.module_path(self.options["views"]["static_path"])
				self.wsgi_app = SharedDataMiddleware(self.wsgi_app, {'/': static_path})
			except:
				pass
		self.wsgi_app = SessionMiddleware(self.wsgi_app, session_options, environ_key="session")
		self.server = WSGIServer((self.options["application"]["address"], self.options["application"]["port"]), self.wsgi_app)
		self.server.serve_forever()
		
	def stop(self):
		self.server.stop()
		
if __name__ == "__main__":
	app = Application()
	app.start()
