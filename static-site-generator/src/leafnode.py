#!/usr/bin/env python

from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    """_summary_

    Args:
        HTMLNode (_type_): _description_
    """


    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag, value, None, props)
        if value == None:
            raise ValueError("Value argument is required")


    def to_html(self):
        if self.tag == None or not self.tag:
            return self.value
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"


    def __eq__(self, other):
        return (
            self.value == other.value
            and self.tag == other.tag
            and self.props == other.props
        )


def main():
    leaf1 = LeafNode("b", "Bold text")
    leaf2 = LeafNode(None, "Normal text")
    leaf3 = LeafNode("i", "Italic text")
    leaf4 = LeafNode(None, "More text")
    leaf5 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})

    print(f"leaf1: {leaf1}")
    print(f"     : {leaf1.to_html()}")

    print(f"leaf2: {leaf2}")
    print(f"     : {leaf2.to_html()}")

    print(f"leaf3: {leaf3}")
    print(f"     : {leaf3.to_html()}")

    print(f"leaf4: {leaf4}")
    print(f"     : {leaf4.to_html()}")

    print(f"leaf5: {leaf5}")
    print(f"     : {leaf5.to_html()}")


if __name__ == "__main__":
    main()
