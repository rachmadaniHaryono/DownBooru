__author__ = 'zerocchi'

from parser.booru import Gelbooru, Danbooru, Safebooru, Konachan, Rule34, Yandere

import util
import getpass
import os
import sys
import urllib.request


def runbooru(tags, limit=0, booru="Danbooru"):
    processors = {f.__name__: f for f in (Danbooru, Gelbooru, Konachan, Yandere, Safebooru, Rule34)}
    if booru in processors:
        tag = processors.get(booru, Danbooru)(tags, limit)
    return tag

if __name__ == "__main__":
    try:
        script, tag, limit, booru = sys.argv
        tag = runbooru(tag, limit, booru)
        util.makefile("/home/%s/Downloads/Downbooru" % getpass.getuser())  # Make file if it doesn't exist
        # Download each images from parsed URLs
        [urllib.request.urlretrieve(url, "{0}/{1}".format(os.getcwd(), url.split("/")[-1])) for url in tag.parse()]
    except ValueError:
        print(util.dochelp.__doc__)