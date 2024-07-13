#!/usr/bin/env python

import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parentnode_to_html(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),LeafNode("a", "Click me!", props={"href": "https://www.google.com"})],)
        self.assertEqual(node.to_html(),'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a href="https://www.google.com">Click me!</a></p>')


    def test_parentnode_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p",)


    def test_parentnode_nested_parents(self):
        # Define some nodes
        child_leaf1 = LeafNode("b", "Bold text")
        child_leaf2 = LeafNode(None, "Normal text")
        child_leaf3 = LeafNode("i", "Italic text")
        child_leaf4 = LeafNode(None, "More text")
        child_leaf5 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})

        # Nest a ParentNode within another ParentNode
        inner_parent = ParentNode("div", [child_leaf1, child_leaf2])
        outer_parent = ParentNode("p", [inner_parent, child_leaf3, child_leaf4, child_leaf5])

        # Get the HTML output
        self.assertEqual(outer_parent.to_html(), '<p><div><b>Bold text</b>Normal text</div><i>Italic text</i>More text<a href="https://www.google.com">Click me!</a></p>')


if __name__ == "__main__":
    unittest.main()
