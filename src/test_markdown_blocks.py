import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bold text**

Do you need _help_ with `this code`?
I don't know.

- This is a list
- Whats up.
"""

        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bold text**",
                "Do you need _help_ with `this code`?\nI don't know.",
                "- This is a list\n- Whats up."
            ]
        )
    def test_block_to_block_type(self):
        block_heading = """### Hello There
Young traveler.
"""
        block_code = """```
What is happening here?
Bruh what.
```
"""
        block_quote = """>Hey. What it UP
> I need some help, thank you.
"""
        block_unordered_list = """- I need this
- I need that
- But I also need this, thank you.
"""
        block_ordered_list = """1. This is the first line
2. This is the second.
3. And this is the third.
4. And this
5. And maybe this as well.
"""
        block_paragraph = """9129 i12 AWOdohiwaoihw wad
wadawdoijawd po
"""
        self.assertEqual(block_to_block_type(block_heading), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block_code), BlockType.CODE)
        self.assertEqual(block_to_block_type(block_quote), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(block_unordered_list), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(block_ordered_list), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(block_paragraph), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()