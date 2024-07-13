#!/usr/bin/env python

import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_eq(self):
        node = HTMLNode("qwerty", "qwerty", "qwerty", "qwerty")
        node2 = HTMLNode("qwerty", "qwerty", "qwerty", "qwerty")
        self.assertEqual(node, node2)


    def test_htmlnode_noteq(self):
        node = HTMLNode("qwerty", "qwerty", "qwerty", "qwerty")
        node2 = HTMLNode("qwert", "qwert", "qwert", "qwert")
        self.assertNotEqual(node, node2)


    def test_htmlnode_repr(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank", "foo": "bar"})
        self.assertEqual(str(node), node.__repr__())


    def test_htmlnode_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank", "foo": "bar"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" foo="bar"')


if __name__ == "__main__":
    unittest.main()
