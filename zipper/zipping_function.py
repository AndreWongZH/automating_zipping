import os
import shutil


def zip_dir(pathname):
    base_name = pathname
    #.split() gives [path to the parent dir, dir to zip]
    root_dir, base_dir = os.path.split(pathname)

    print(f"zipping dir {base_dir} now ....")

    shutil.make_archive(base_name=base_name, format='zip', base_dir=base_dir, root_dir=root_dir)

    print(f"The directory {base_dir} has been zipped at {root_dir}\n")


