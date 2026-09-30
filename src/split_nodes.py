from text_node import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_text = old_node.text.split(delimiter)
        len_split_text = len(split_text)
        if len_split_text % 2 != 1: # If there is not an odd number of texts; AKA no closing delimiter
            raise ValueError(f'Could not find closing delimiter for {delimiter}')
        for i in range(len_split_text):
            if i % 2 == 1: # If index is odd (text inside of delimiters)
                new_nodes.append(TextNode(split_text[i], text_type))
            elif not split_text[i] == "":
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_images(old_node.text)
        if matches:
            current_text = old_node.text
            for match in matches:
                split_text = current_text.split(f'![{match[0]}]({match[1]})', 1)
                if split_text[0] != "":
                    new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
                current_text = split_text[1]
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_links(old_node.text)
        if matches:
            current_text = old_node.text
            for match in matches:
                split_text = current_text.split(f'[{match[0]}]({match[1]})', 1)
                if split_text[0] != "":
                    new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
                current_text = split_text[1]
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes