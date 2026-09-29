from text_to_text_nodes import text_to_textnodes
from htmlnode import HTMLNode
from markdown_blocks import block_to_block_type, markdown_to_blocks, BlockType
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type
        html_node: HTMLNode
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = HTMLNode("p", block)
            case BlockType.HEADING:
                html_node = HTMLNode("h", block)
            case BlockType.CODE:
                html_node = HTMLNode("code", block)
            case BlockType.QUOTE:
                html_node = HTMLNode("blockquote", block)
            case BlockType.UNORDERED_LIST:
                html_node = HTMLNode("ul", block)
            case BlockType.ORDERED_LIST:
                html_node = HTMLNode("ol", block)
            case _:
                raise Exception("No valid BlockType")
        

def text_to_children(text):
    htmlnode_list = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        htmlnode_list.append(text_node.text_node_to_html_node())
    return htmlnode_list