import os

from jinja2 import Environment, FileSystemLoader, select_autoescape


class Template:

    env: Environment

    name: str

    def __init__(self, name: str):
        self.name = name
        base_path = os.path.join(os.path.dirname(__file__), "templates")
        self.env = Environment(
            loader=FileSystemLoader(base_path),
            autoescape=select_autoescape(["html", "jinja"]),
        )

    def html(self, *, title: str = "", data: dict = {}):
        template = self.env.get_template(f"{self.name}")
        html = template.render(title=title, data=data)
        return html
