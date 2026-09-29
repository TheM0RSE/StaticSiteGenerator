from text_node import TextType, TextNode
import unittest
from text_to_text_nodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        textnodes1 = text_to_textnodes("This is `coding` and **bold text**")
        textnodes2 = text_to_textnodes("**BOLD**. I need _italic_ in my life ![help](https://i.imgur.com/fJRm4Vk.jpeg)")
        textnodes3 = text_to_textnodes("[What](https://www.google.com) is wrong with `this code`...")
        
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("coding", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
            ],
            textnodes1
        )
        self.assertListEqual(
            [
                TextNode("BOLD", TextType.BOLD),
                TextNode(". I need ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" in my life ", TextType.TEXT),
                TextNode("help", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            textnodes2
        )
        self.assertListEqual(
            [
                TextNode("What", TextType.LINK, "https://www.google.com"),
                TextNode(" is wrong with ", TextType.TEXT),
                TextNode("this code", TextType.CODE),
                TextNode("...", TextType.TEXT),
            ],
            textnodes3
        )

if __name__ == "__main__":
    unittest.main()