#!/usr/bin/env python

import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_pass_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')


    def test_pass_to_html_with_props(self):
        node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


    def test_fail_to_html(self):
        node = LeafNode("p", "This is a paragraph of text", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), ' href="https://www.google.com" target="_blank" foo="bar!"')


    def test_fail_to_html_no_tag(self):
        node = LeafNode(value="This is a paragraph of text", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), ' href="https://www.google.com" target="_blank" foo="bar!"')


    def test_error_to_html_no_value(self):
        node = LeafNode(tag="a", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), ' href="https://www.google.com" target="_blank" foo="bar!"')


if __name__ == "__main__":
    unittest.main()
