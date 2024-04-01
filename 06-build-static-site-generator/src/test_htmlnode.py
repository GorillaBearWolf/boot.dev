#!/usr/bin/env python

import unittest

from htmlnode import HTMLnode


class TestHtmlNode(unittest.TestCase):
    def test_true_props_to_html(self):
        node = HTMLnode(props={"href": "https://www.google.com", "target": "_blank", "foo": "bar"})
        self.assertEqual(node.props_to_html(), f' href="https://www.google.com" target="_blank" foo="bar"')


    def test_false_props_to_html(self):
        node = HTMLnode(props={"href": "https://www.google.com", "target": "_blank", "foo": "bar"})
        self.assertEqual(node.props_to_html(), f' href="https://www.google.com" target="_blank" foo="bar!"')



if __name__ == "__main__":
    unittest.main()
