from textnode import TextNode,TextType



def main() -> None:
    text = TextNode("This is some text",TextType.LINK,"https://www.google.com")
    print(text)


main()