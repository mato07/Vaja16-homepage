#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2 # lahko so rdeci ker v resnici poganja googlov python
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None): # pod params lahko dodamo argumente za spletno stran
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("homepage.html")

class MainHandler1(BaseHandler):
    def get(self):
        return self.render_template("o-meni.html")

class MainHandler2(BaseHandler):
    def get(self):
        return self.render_template("moji-projekti.html")

class MainHandler3(BaseHandler):
    def get(self):
        return self.render_template("blog.html")

class MainHandler4(BaseHandler):
    def get(self):
        return self.render_template("kontakt.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/o-meni', MainHandler1),
    webapp2.Route('/moji-projekti', MainHandler2),
    webapp2.Route('/blog', MainHandler3),
    webapp2.Route('/kontakt', MainHandler4)
], debug=True)
