from extract_title import extract_title
from markdown_html import markdown_to_html_node
import shutil
import os
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    delete_contents("docs")
    copy_contents("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = ""
    template = ""

    with open(from_path, "r", encoding="utf-8") as file:
        markdown = file.read()

    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    template = template.replace('href="/', f'href="{base_path}')
    template = template.replace('src="/', f'src="{base_path}')

    print(markdown + "\n---------------\n" + template)

    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    content = os.listdir(dir_path_content)
    for item in content:
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path) and item.endswith(".md"):
            generate_page(item_path, template_path, os.path.join(dest_dir_path, item.rstrip(".md")+".html"), base_path)
        elif os.path.isdir(item_path):
            new_dir_path = os.path.join(dest_dir_path, item)
            os.mkdir(new_dir_path)
            generate_pages_recursive(item_path, template_path, new_dir_path, base_path)

def delete_contents(path: str):
    if os.path.isdir(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        raise ValueError(f"path: '{path}' is not a valid path/directory")

def copy_contents(copy_path: str, paste_path: str):
    if os.path.isdir(copy_path):
        if os.path.isdir(paste_path):
            copy_contents_helper(copy_path, paste_path, copy_path)
        else:
            raise ValueError(f"paste_path: '{paste_path}' is not a valid path")
    else:
        raise ValueError(f"copy_path: '{copy_path}' is not a valid path")

def copy_contents_helper(copy_path: str, paste_path: str, current_path: str):
    contents = os.listdir(current_path)
    if contents:
        for content in contents:
            content_path = os.path.join(current_path, content)
            if os.path.isfile(content_path):
                new_file_path = os.path.join(paste_path, os.path.relpath(content_path, copy_path))
                shutil.copy(content_path, new_file_path)
                print(f"File created: {new_file_path}")
            elif os.path.isdir(content_path):
                new_dir_path = os.path.join(paste_path, os.path.relpath(content_path, copy_path))
                os.mkdir(new_dir_path)
                print(f"Directory created: {new_dir_path}")
                copy_contents_helper(copy_path, paste_path, content_path)
            else:
                raise Exception("Error: Not a file or a directory")
main()