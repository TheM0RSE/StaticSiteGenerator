from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "orderered list"

def block_to_block_type(md: str) -> BlockType:
    # HEADING
    if re.findall(r"^#{1,6} ", md): # Starts with 1-6 hashtags and a space
        return BlockType.HEADING
    
    # CODE
    if re.findall(r"^`{3}[\s\S]*?\n[\s\S]*?`{3}$", md): # Starts and ends with three backticks with atleast one new line in the middle
        return BlockType.CODE
    
    # Split markdown into lines to check for Quote, Unordered- and Ordered List
    lines = md.splitlines()

    # QUOTE
    if all(line.startswith(">") for line in lines if line): # Every line starts with ">"
        return BlockType.QUOTE

    # UNORDERED LIST
    if all(line.startswith("- ") for line in lines if line): # Every line starts with "- "
        return BlockType.UNORDERED_LIST
    
    # ORDERED LIST
    expected_num = 1
    for line in lines:
        if line.startswith(f"{expected_num}. "): # Does line start with expected number?
            expected_num += 1
        else:
            break
    if expected_num - 1 == len(lines): # If each line was numbered in order
        return BlockType.ORDERED_LIST
    
    # Met none of the conditions
    return BlockType.PARAGRAPH
        

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block != "":
            block = block.strip()
            new_blocks.append(block)
    return new_blocks