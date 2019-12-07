import json

# Testing coverage in the unittests of classes, this should never be indentently called
class ResourceAccessor:
    def __init__(self,resource,area=False):
        if area:
            location = "../Resources/" + area + "/" + resource + ".JSON"
        else:
            location = "../Resources/" + resource + ".JSON"
        self.resource = self.open_json(location)

    @staticmethod
    def open_json(json_path):
        with open(json_path) as json_file:
            return json.load(json_file)

    #TODO Give access and return methods

print(ResourceAccessor("StandardDeck").resource["cards"]["stars"])