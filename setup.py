from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "kiss.py",
    version = "0.3.3",
    author = "Stanislav Feldman",
    description = ("MVC web framework in Python with Gevent, Jinja2, Werkzeug"),
    url = "http://stanislavfeldman.github.com/kiss.py/",
    keywords = "web framework gevent jinja2 werkzeug orm oauth socialauth vkontakte facebook google",
    packages=[
    	"kiss", "kiss.controllers", "kiss.core", "kiss.views", "kiss.models"
    ],
    install_requires = ["gevent", "jinja2", "compressinja", "beaker", "werkzeug", "putils", "jsmin", "pyScss", "peewee", "jsonpickle"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
)
