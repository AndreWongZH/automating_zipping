"""
two options: zip one directory or zip multiple directories
To choose, input either "one" or "multiple"

To zip multiple directories, pathname given must lead to the main directory that contains all the directories to zip

"""
from os_navigation.directory_navigation import get_all_dir
from zipper.zipping_function import zip_dir

while True:
    print("Do you want to zip one or multiple directories?")
    one_or_more = input("type <one> or <multiple>: ")

    if one_or_more.lower() == "one":
        print("\nPlease provide the pathname to the directory")
        pathname = input("Input here: ")

        #zip the directory
        zip_dir(pathname=pathname)

        break
    elif one_or_more.lower() == "multiple":
        print("\nPlease provide the pathname to the main directory")
        pathname = input("Input here: ")

        #get all the pathnames of directories to zip
        list_of_dir = get_all_dir(pathname=pathname)

        #zip each directory
        for each_dir in list_of_dir:
            zip_dir(pathname=each_dir)

        break
    else:
        print("\nError, please enter either <one> or <multiple>\n")

