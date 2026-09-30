import shutil
import os

def main():
    delete_contents("public")
    copy_contents("static", "public")

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
            elif os.path.isdir(content_path):
                new_dir_path = os.path.join(paste_path, os.path.relpath(content_path, copy_path))
                os.mkdir(new_dir_path)
                copy_contents_helper(copy_path, paste_path, content_path)
            else:
                raise Exception("Error: Not a file or a directory")
main()