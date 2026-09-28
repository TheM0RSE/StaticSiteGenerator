class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list | None = None, props: dict | None = None):
        self.tag = tag # HTML tag
        self.value = value # Value of HTML tag
        self.children = children # List with the HTMLNode-children of this node
        self.props = props # Dictionary of attributes in HTML tag
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        if not self.props:
            return ""
        return f' href="{self.props["href"]}" target="{self.props["target"]}"'
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict | None = None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode is missing value")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict | None = None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode is missing tag")
        if not self.children:
            raise ValueError("ParentNode is missing children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f'<{self.tag}>{children_html}</{self.tag}>'