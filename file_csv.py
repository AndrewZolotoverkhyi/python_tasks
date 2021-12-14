import csv


class Csv(object):
    def __init__(self, name, website, born):
        self.name = name
        self.website = website
        self.born = born


object1 = Csv('name', 'website', 'born')

with open('file.csv', 'w') as f:
    writer = csv.writer(f)
    for row in object1.__dict__:
        writer.writerow(row)

with open('file.csv') as f:
    print(f.read())