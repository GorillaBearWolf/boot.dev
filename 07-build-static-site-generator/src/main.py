#!/usr/bin/env python

from textnode import TextNode


def main():
    node = TextNode("Ipsum lorem", "bold", "http://www.refsnider.me")
    print(f"textnode: {node}")


if __name__ == "__main__":
    main()
