import json


class ResourceAccessor:
    def __init__(self,area):
        self.area = area

    @staticmethod
    def open_json(json_path):
        with open(json_path) as json_file:
            return json.load(json_file)
