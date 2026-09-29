import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is a test to extract ![THIS IMAGE](https://i.imgur.com/zjjcJKZ.png), yeah. Hope it works"
        )
        self.assertListEqual(matches, [("THIS IMAGE", "https://i.imgur.com/zjjcJKZ.png")])
    def test_extract_markdown_images(self):
        matches = extract_markdown_links(
            "This is a test to extract [this link](https://www.google.com), yeah. Hope it works"
        )
        self.assertListEqual(matches, [("this link", "https://www.google.com")])
if __name__ == "__main__":
    unittest.main()