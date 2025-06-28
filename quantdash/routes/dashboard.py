import tornado

from quantdash.template import Template


class DashboardHandler(tornado.web.RequestHandler):

    def get(self):
        html = Template(name="routes/dashboard.jinja2").html()
        self.write(html)
