import json


class Json(object):
    def __init__(self, name,website, born):
        self.name = name
        self.website = website
        self.born = born


object1 = Json('name', 'website', 'born')

with open('data.json', 'w') as outfile:
    json.dump(object1.__dict__, outfile)

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in object1.__dict__:
        print(p)