#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

__author__ = 'zerocchi'

from parser.booru import Gelbooru, Danbooru, Safebooru, Konachan, Rule34, Yandere

import util
import getpass
import os
import sys
import urllib.request
from argparse import ArgumentParser

def runbooru(tags, limit=0, booru="Danbooru"):
    processors = {f.__name__: f for f in (Danbooru, Gelbooru, Konachan, Yandere, Safebooru, Rule34)}
    if booru in processors:
        tag = processors.get(booru, Danbooru)(tags, limit)
    return tag

def parse_args(args):
    parser = ArgumentParser(description='Simple Imageboard CLI Downloader..')
    parser.add_argument('tags', metavar='<tags>', help='Tags can be as simple as character name or by adding extra tag wrapped in quotation mark.')
    parser.add_argument('limit', metavar='<limit>', help='Limit of images to download.')
    parser.add_argument('booru', metavar='<booru>', help='Preferred image board.')
    parser.add_argument('--dir', default=os.getcwd(), help='Download folder.')
    parsed_argument = parser.parse_args(args)
    
    return parsed_argument


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
        tag = runbooru(args.tags, args.limit, args.booru)
        util.makefile(args.dir)  # Make file if it doesn't exist
        # Download each images from parsed URLs
        [urllib.request.urlretrieve(url, "{0}/{1}".format(os.getcwd(), url.split("/")[-1])) for url in tag.parse()]
    except ValueError:
        print(util.dochelp.__doc__)