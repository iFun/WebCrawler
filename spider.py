#from six.moves.urllib.parse import urlparse
import urlparse
#from urllib.requet import urlopen
from link_finder import LinkFinder
from general import *

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
        create_data_files(Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page():
        if page_url not in Spider.crawled:
            print(thread_name + 'now crawling' + page_url)
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
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: cannot crawl page: ' + page_url)
            return set()

        #return all the link in the crawled page   
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
            for url in links:
                if url in Spider.queue:
                    continue
                if url in Spider.crawled:
                    continue
                if Spider.domain_name not in url:
                    continue
                Spider.queue.add(url)
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        











