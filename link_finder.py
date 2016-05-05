from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, message):
        super().__init__()
    def handle_starttage(self,tag,attrs):
        if tag == 'a':
            for (at)

    def error(self,message):
        pass

finder = LinkFinder()
