from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
        self.tag = tag
        self.value = value
        self.props = props


    def to_html(self):
        if not self.value:
            raise ValueError("value cannot be None")
        if self.props:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'