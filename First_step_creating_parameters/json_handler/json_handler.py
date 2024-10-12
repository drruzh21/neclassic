from typing import Any
from re import sub


class JsonHandler:
    PROHIBITED_SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+",
                          "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"]

    def __init__(self, data: list[dict[str, Any]]):
        self.data = data
        self.keys: dict[str, int] = {}

    def handle(self):
        self._prepare_data()
        self._handle_data()

    def _prepare_json_key(self, key: str) -> str:
        new_key = key
        for symbol in self.PROHIBITED_SYMBOLS:
            new_key = new_key.replace(symbol, "")
        new_key = new_key.lower().replace(",", ".").strip().replace(" ", "_")
        new_key = sub(r"(.)\1{2,}", r"\1", new_key)

        return new_key

    def _prepare_json(self, data: dict[str, Any]) -> dict[str, Any]:
        temp_json = {}
        for key, value in data.items():
            temp_json[self._prepare_json_key(key)] = value

        return temp_json

    def _prepare_data(self):
        self.data = [self._prepare_json(json) for json in self.data]

    def _handle_json(self, json: dict[str, Any]):
        for key in json:
            if key in self.keys:
                self.keys[key] += 1
            else:
                self.keys[key] = 1

    def _handle_data(self):
        for json in self.data:
            self._handle_json(json)
