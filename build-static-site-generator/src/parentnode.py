#!/usr/bin/env python

from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    """_summary_

    Args:
        HTMLNode (_type_): _description_
    """


    def __init__(self, tag=None, children=[], props=None) -> None:
        super().__init__(tag, None, children, props)
        if not children:
            raise ValueError("Children argument is required")


    def to_html(self):
        if not self.tag:
            raise ValueError("No tag provided")
        if not self.children:
            raise ValueError("No children found")

        children_html = ''
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}>{children_html}</{self.tag}>"


def main():
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
    ],
)
    print(node)
    print(node.to_html())


if __name__ == "__main__":
    main()
