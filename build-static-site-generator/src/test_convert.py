#!/usr/bin/env python

import unittest

from convert import text_node_to_html_node
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_link,
    text_type_image
    )

def test_text_node_to_html_node():
    # Test text type
    text_node = TextNode(text_type_text, "Hello World", None)
    html_node = text_node_to_html_node(text_node)
    assert html_node.value == "Hello World"
    assert html_node.tag is None

    # Test bold type
    text_node = TextNode(text_type_bold, "Bold Text", None)
    html_node = text_node_to_html_node(text_node)
    assert html_node.value == "Bold Text"
    assert html_node.tag == "b"

    # Test link type with valid props
    text_node = TextNode(text_type_link, "Link Text", {"href": "https://example.com"})
    html_node = text_node_to_html_node(text_node)
    assert html_node.value == "Link Text"
    assert html_node.tag == "a"
    assert html_node.props["href"] == "https://example.com"

    # Test link type with missing href
    try:
        text_node = TextNode(text_type_link, "Link Text", {})
        text_node_to_html_node(text_node)
    except KeyError as e:
        print(f"Caught expected exception: {e}")

    # Test image type with valid props
    text_node = TextNode(text_type_image, None, {"src": "image.png", "alt": "An image"})
    html_node = text_node_to_html_node(text_node)
    assert html_node.value is None
    assert html_node.tag == "img"
    assert html_node.props["src"] == "image.png"
    assert html_node.props["alt"] == "An image"

    # Test image type with missing props
    try:
        text_node = TextNode(text_type_image, None, {"src": "image.png"})
        text_node_to_html_node(text_node)
    except KeyError as e:
        print(f"Caught expected exception for missing src: {e}")
