import json

class Resource_Manager:
    def __init__(self,*args):
        self.path = f"~/Resources/"
        for path_modifier in args:
            self.path += f"{path_modifier}/"

    def open_json_file(self):
        with open(self.path) as file_path:
            return json.load(file_path)