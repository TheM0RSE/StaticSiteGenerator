from text_to_text_nodes import text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_blocks import block_to_block_type, markdown_to_blocks, BlockType
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node: HTMLNode
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = ParentNode("p", text_to_children(block.replace("\n", " ")))
            case BlockType.HEADING:
                hashtag_amount = len(re.match(r"^(#+)", block).group(1))
                html_node = ParentNode(f"h{hashtag_amount}", text_to_children(block.lstrip("# ")))
            case BlockType.CODE:
                html_node = ParentNode("pre", [LeafNode("code", re.sub(r"`{3}$" ,"", re.sub(r"^`{3}\n", "", block)))])
            case BlockType.QUOTE:
                html_node = ParentNode("blockquote", text_to_children(block.lstrip("> ").replace("\n> ", " ")))
            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                unordered_list = []
                for line in lines:
                    unordered_list.append(ParentNode("li", text_to_children(re.sub(r"^\- ", "", line))))
                html_node = ParentNode("ul", unordered_list)
            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                ordered_list = []
                for line in lines:
                    ordered_list.append(ParentNode("li", text_to_children(re.sub(r"^\d+\. ", "", line))))
                html_node = ParentNode("ol", ordered_list)
            case _:
                raise Exception("No valid BlockType")
        block_children.append(html_node)
    return ParentNode("div", block_children)
        

def text_to_children(text):
    htmlnode_list = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        htmlnode_list.append(text_node.text_node_to_html_node())
    return htmlnode_list