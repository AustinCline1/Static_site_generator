import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    prop_dict1 = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    def test_(self):
        node = HTMLNode("","","",self.prop_dict1)
        node2 = HTMLNode("","","",None)
        print(node.props_to_html())
        print(node2.props_to_html())


if __name__ == '__main__':
    unittest.main()
