__author__ = 'zerocchi'

from bs4 import BeautifulSoup
try:
    from urllib.request import Request, urlopen, HTTPError  # Python 3
except:
    from urllib2 import Request, urlopen, HTTPError  # Python 2
import requests

class ImageNotFoundError(Exception):
    """Exception raised when image not found in page"""

class TagsNotFoundError(Exception):
    """Exception raised when image with tags not found in page"""

class Booru:

    @staticmethod
    def get_data(url):
        """
        :param url: pass full url to get the JSON/XML raw data
        :return: JSON/XML raw data
        """
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response)
        return soup

    def parse(self):
        """
        parse() method return a list consists of images URL.
        :return: list of images URL.
        """
        raise NotImplementedError("parse() method not implemented.")

class Sankakuidol(Booru): 
    base_url = u'https://idol.sankakucomplex.com'
    api_url = u'/?tags={0}&page={1}'       
    def __init__(self, tags, limit):
        self.tags = tags
        self.limit = limit
        
        
    def parse(self):
        links = []
        url_template = self.base_url + self.api_url
        # search tag(s) with first page
        page_num = 1 
        # TODO: check if self.limit = 0
        try :
            img_links = []
            while len(img_links) < self.limit :
                url = url_template.format(self.tags, str(page_num))
                # 1 page contain 20 image links
                url_soup = super(Booru,self).get_data(url)
                self.url_soup = url_soup
                if url_soup is None :
                    raise ImageNotFoundError
                img_links = filter(lambda x: x.parent.get('class')[0] != 'popular-preview-post',
                  url_soup.find_all('span', {'class':'thumb'}))
                self.img_links = img_links
                
                if len(img_links) == 0 and page_num == 1:
                    raise TagsNotFoundError('Tags not found') 
                elif len(img_links) >self.limit and page_num !=1:
                    raise ImageNotFoundError('Image end at page {0}'.format(page_num-1))
                
                for link in img_links : # parse the found links
                    html = super().get_data(self.base_url + link)
                    if len(links)< self.limit :
                        links.append(html.find('a', {'id':'highres'}).get('href')[0])
                page_num += 1
        except ImageNotFoundError:
            pass
    
class Gelbooru(Booru):

    base_url = "http://gelbooru.com"
    api_url = u"/index.php?page=dapi&s=post&q=index&tags={0}&limit={1}"

    def __init__(self, tags, limit):
        self.url = self.base_url + self.api_url.format(tags, limit)

    def parse(self):
        img_key = 'post'
        data = super().get_data(self.url)
        links = [dict(post.attrs)['file_url'] for post in data.findAll(img_key)]
        return links


class Danbooru(Booru):

    base_url = "https://danbooru.donmai.us"
    api_url = "/posts.xml?tags={0}&limit={1}"

    def __init__(self, tags, limit):
        tags = tags.split()
        self.url = self.base_url + self.api_url.format("+".join(tags), limit)

    def parse(self):
        data = super().get_data(self.url)
        links = [self.base_url + post.find('file-url').string.strip() for
                 post in data.findAll('post') if post is not None]
        return links

class Konachan(Gelbooru):

    base_url = "http://konachan.com"
    api_url = "/post.xml?tags={0}&limit={1}"

    def __init__(self, tags, limit):
        super().__init__(tags, limit)

    def parse(self):
        img_key = 'file_url'
        links = super().parse()
        return links


class Safebooru(Gelbooru):

    base_url = "http://safebooru.org"

    def __init__(self, limit, tags):
        super().__init__(limit, tags)


class Rule34(Gelbooru):

    base_url = "http://rule34.xxx"

    def __init__(self, tags, limit):
        super().__init__(tags, limit)


class Yandere(Konachan):

    base_url = "http://yande.re"

    def __init__(self, tags, limit):
        super().__init__(tags, limit)
