#!/usr/bin/env python

from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__()
        self.value = value
        self.tag = tag
        self.props = props

    # def __init__(self, value, tag=None, props=None) -> None:
    #     self.value = value
    #     self.tag = tag
    #     self.props = props
