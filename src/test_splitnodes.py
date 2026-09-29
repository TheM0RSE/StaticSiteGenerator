from textnode import TextType, TextNode
import unittest
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node_bold = TextNode("Hello *world*, bruh", TextType.TEXT)
        node_italic = TextNode("_IDK_ what to do", TextType.TEXT)
        node_code = TextNode("I think `my code` is broken", TextType.TEXT)
        node_text = TextNode("Hello, what is up?", TextType.CODE)
        nodes = [node_bold, node_italic, node_code, node_text]
        self.assertEqual(
            split_nodes_delimiter(nodes, "*", TextType.BOLD), 
            [TextNode("Hello ", TextType.TEXT), 
            TextNode("world", TextType.BOLD), 
            TextNode(", bruh", TextType.TEXT), 
            node_italic, 
            node_code,
            node_text]
        )
    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ]
        )
    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ]
        )


if __name__ == "__main__":
    unittest.main()