#!/usr/bin/env python3

from leafnode import LeafNode
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == text_type_text:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("text_type not recognized")


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes += node
        elif delimiter == None:
            raise Exception
        else:
            split_node = node.text.split(delimiter)
            new_nodes.extend(TextNode(split_node[0], text_type_text))
            new_nodes.extend(TextNode(split_node[1], text_type))
            new_nodes.extend(TextNode(split_node[2], text_type_text))



def main():
    node1 = TextNode("Ipsum lorem", "text", "http://www.refsnider.me")
    node2 = TextNode("Ipsum lorem", "bold", "http://www.refsnider.me")
    node3 = TextNode("Ipsum lorem", "italic", "http://www.refsnider.me")
    node4 = TextNode("Ipsum lorem", "code", "http://www.refsnider.me")
    node5 = TextNode("Ipsum lorem", "link", "http://www.refsnider.me")
    node6 = TextNode("Ipsum lorem", "image", "http://www.refsnider.me")
    print(text_node_to_html_node(node1))
    print(text_node_to_html_node(node2))
    print(text_node_to_html_node(node3))
    print(text_node_to_html_node(node4))
    print(text_node_to_html_node(node5))
    print(text_node_to_html_node(node6))


if __name__ == "__main__":
    main()

