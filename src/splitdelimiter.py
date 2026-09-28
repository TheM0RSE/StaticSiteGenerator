from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        split_text = old_node.text.split(delimiter)
        len_split_text = len(split_text)
        if len_split_text % 2 != 1: # If there is not an odd number of texts; AKA no closing delimiter
            raise Exception(f'Error: Could not find closing delimiter for {delimiter}')
        for i in range(len_split_text):
            if i % 2 == 1: # If index is odd (text inside of delimiters)
                new_nodes.append(TextNode(split_text[i], text_type))
            else:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
    return new_nodes

