from json import loads

from json_handler import JsonHandler


class StringHandler(JsonHandler):
    def __init__(self, data: list[str]):
        super().__init__([loads(jsonstring) for jsonstring in data])
