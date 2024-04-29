#!/usr/bin/env python

import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_pass_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank", "foo": "bar"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" foo="bar"')


    def test_fail_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank", "foo": "bar"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" foo="bar!"')



if __name__ == "__main__":
    unittest.main()
