from textnode import TextType, TextNode
import unittest
from splitdelimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()