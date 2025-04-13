import shutil

from textnode import TextNode,TextType
import os

dir_path_static = "./static"
dir_path_public = "./public"


def copy(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        to_path = os.path.join(destination, filename)
        print(f" * from: {from_path} to: {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy(from_path, to_path)

def main() -> None:
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files...")
    copy(dir_path_static, dir_path_public)


main()