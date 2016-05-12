from urllib import urlopen
import urlparse
from link_finder import LinkFinder
from general import *
from domain import *
import urllib


class Spider:

    # Class variables (shared among all instances)
    # set the variable later on
    porject_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()



    def __init__(self, porject_name, base_url, domain_name):
        Spider.porject_name = porject_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.porject_name + '/queue.txt'
        Spider.crawled_file = Spider.porject_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.porject_name)
        create_data_file(Spider.porject_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + 'now crawling ' + page_url)
            print('Queue' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
    
    @staticmethod
    def gather_link(page_url):
        html_string = ''
        # goto website, get the byte data convert to string
        # pass it through to linkfinder, and find all the links
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.get_header('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()


    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        











