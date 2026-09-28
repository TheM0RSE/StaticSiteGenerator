import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("h1", "testing")
        node2 = HTMLNode("h1", "testing")
        node3 = HTMLNode("a", "omg", [], {"href": "https://www.google.com", "target": "_blank"})
        node4 = HTMLNode("a", "hello", [], {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node.props_to_html(), node3.props_to_html)
        self.assertEqual(node3.props_to_html(), node4.props_to_html())
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Link to Google", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com" target="_blank">Link to Google</a>')
    def test_to_html_with_children(self):
        child_node = LeafNode("b", "hello")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><b>hello</b></div>")
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("span", "yo")
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><div><span>yo</span></div></div>")
if __name__ == "__main__":
    unittest.main()