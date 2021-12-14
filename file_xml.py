from lxml import etree


class Xml(object):
    def __init__(self, name, website):
        self.name = name
        self.website = website


object1 = etree.Element("object1")
object1.set('Lubomir', 'nachalnikoop.com')

my_tree = etree.ElementTree(object1)
with open('file.xml', 'wb') as f:
    f.write(etree.tostring(my_tree))

my_tree = etree.parse("file.xml")
root = my_tree.getroot()