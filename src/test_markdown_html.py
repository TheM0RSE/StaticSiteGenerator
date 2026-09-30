import unittest
from markdown_html import markdown_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_headings(self):
        md = """
## Hello **human**

# I need this _please_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Hello <b>human</b></h2><h1>I need this <i>please</i></h1></div>"
        )
    def test_quotes(self):
        md = """
> Who `needs` this, **bruh**
> _Who thinks like that_ hmm?
> I would think we don't need it.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Who <code>needs</code> this, <b>bruh</b> <i>Who thinks like that</i> hmm? I would think we don't need it.</blockquote></div>"
        )
    def test_ordered_list(self):
        md = """
1. This is my **first** item.
2. I `need` some help with the second?
3. And why do you need a _third_ one?
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is my <b>first</b> item.</li><li>I <code>need</code> some help with the second?</li><li>And why do you need a <i>third</i> one?</li></ol></div>"
        )
    def test_unordered_list(self):
        md = """
- This is the `first item`.
- And this is the **second**.
- Why do i need this many items, _bruh_.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is the <code>first item</code>.</li><li>And this is the <b>second</b>.</li><li>Why do i need this many items, <i>bruh</i>.</li></ul></div>"
        )
if __name__ == "__main__":
    unittest.main()