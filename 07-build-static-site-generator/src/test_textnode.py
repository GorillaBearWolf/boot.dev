#!/usr/bin/env python

import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_textnode_eq_nodes(self):
        node = TextNode("This is a text node", "text", None)
        node2 = TextNode("This is a text node", "text", None)
        self.assertEqual(node, node2)


    def test_textnode_eq_nodes_blank_url(self):
        node = TextNode("This is a text node", "code")
        node2 = TextNode("This is a text node", "code")
        self.assertEqual(node, node2)


    def test_textnode_diff_urls(self):
        node = TextNode("This is a text node", "image", "google.com")
        node2 = TextNode("This is a test node", "image", "espn.com")
        self.assertNotEqual(node, node2)


    def test_textnode_diff_text_type(self):
        node = TextNode("This is a text node", "image", "google.com")
        node2 = TextNode("This is a text node", "link", "google.com")
        self.assertNotEqual(node, node2)


    def test_textnode_diff_text(self):
        node = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a test node", "bold", "google.com")
        self.assertNotEqual(node, node2)


    def test_textnode_eq_str_repr(self):
        node = TextNode("This is a text node", "italic", "espn.com")
        self.assertEqual(str(node), node.__repr__())


if __name__ == "__main__":
    unittest.main()
