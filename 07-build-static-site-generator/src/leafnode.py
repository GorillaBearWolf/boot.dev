#!/usr/bin/env python

from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    """_summary_

    Args:
        HTMLNode (_type_): _description_
    """


    def __init__(self, tag="", value="", props=None) -> None:
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props


    def to_html(self):
        if not self.value:
            raise ValueError("No leaf node value")
        if not self.tag:
            return self.value
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
