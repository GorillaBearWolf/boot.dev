#!/usr/bin/env python

import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leafnode_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')


    def test_leafnode_to_html_with_props(self):
        node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


    def test_fail_leaf_to_html_no_tag(self):
        node = LeafNode(value="This is a paragraph of text", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "This is a paragraph of text")


    def test_leafnode_to_html_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="a", props={"href": "https://www.google.com"})


if __name__ == "__main__":
    unittest.main()
