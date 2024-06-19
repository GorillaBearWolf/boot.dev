#!/usr/bin/env python

from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    """_summary_

    Args:
        HTMLNode (_type_): _description_
    """


    def __init__(self, children, tag="", props=None) -> None:
        super().__init__()
        self.children = children
        self.tag = tag
        self.props = props


    def to_html(self):
        if not self.tag:
            raise ValueError("No tag provided")
        if not self.children:
            raise ValueError("No children found")
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
