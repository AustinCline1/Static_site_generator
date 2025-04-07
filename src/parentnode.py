from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("tag cannot be None")
        if not self.children:
            raise ValueError("children cannot be None")
        parent_list = []
        for child in self.children:
            parent_list.append(child.to_html())
        return f'<{self.tag}{self.props_to_html()}>{"".join(parent_list)}</{self.tag}>'