from textnode import TextType, TextNode

def main():
    dummy = TextNode("This is some text", TextType.bold, "https://www.google.com")
    print(dummy)

main()