import tornado
import json


class HealthHandler(tornado.web.RequestHandler):

    def get(self):
        resp_data = {
            "status": "OK",
            "version": "0.0",
        }
        self.write(json.dumps(resp_data))
