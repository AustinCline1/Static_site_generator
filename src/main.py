import shutil
import os
import sys
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


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
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files...")
    copy(dir_path_static, dir_path_public)

    print("Generating pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public,basepath)


main()