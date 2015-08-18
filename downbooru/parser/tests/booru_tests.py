#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase

#from parser import Sankakuchan
from downbooru.parser.booru import Sankakuchan

class testSankakuchanClass(TestCase):
    @classmethod
    def setUpClass(self):
        self.tag = 'webm'
        self.limit_one_page = 20

    def testSimpleTag(self):
        sc = Sankakuchan(self.tag, self.limit_one_page)
        links = sc.parse()
        assertEqual(len(links),self.limit)
        
