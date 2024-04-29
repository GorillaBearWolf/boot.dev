#!/usr/bin/env python

import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


class TestTextNode(unittest.TestCase):
    def test_pass_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)


    def test_fail_eq_text(self):
        node = TextNode("This is a text node", text_type_image, "google.com")
        node2 = TextNode("This is a test node", text_type_image, "espn.com")
        self.assertEqual(node, node2)


    def test_fail_eq_url(self):
        node = TextNode("This is a text node", text_type_code, "google.com")
        node2 = TextNode("This is a text node", text_type_code, "espn.com")
        self.assertEqual(node, node2)


    def test_fail_eq_text_type(self):
        node = TextNode("This is a text node", text_type_link, "espn.com")
        node2 = TextNode("This is a text node", text_type_bold, "espn.com")
        self.assertEqual(node, node2)


    def test_pass_eq_repr(self):
        node = TextNode("This is a text node", text_type_italic, "espn.com")
        self.assertEqual("TextNode(This is a text node, italic, espn.com)", node.__repr__())


if __name__ == "__main__":
    unittest.main()
