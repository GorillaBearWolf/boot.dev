#!/usr/bin/env python


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """Child classes will override this method to render themselves as HTML."""
        raise NotImplementedError

    def props_to_html(self):
        """This method should return a string that represents the HTML attributes of the node."""
        html_string = ""
        for prop in self.props:
            html_string += f' {prop}="{self.props[prop]}"'
        return html_string

    def __eq__(self, other) -> bool:
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


def main():
    node = HTMLNode()
    print(node)


if __name__ == "__main":
    main()
