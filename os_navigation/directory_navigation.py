import os


#from main dir
def get_all_dir(pathname):
    #get a list of directories only
    list_of_dir = [os.path.join(pathname, each_dir) for each_dir in os.listdir(path=pathname) if os.path.isdir(os.path.join(pathname, each_dir))]
    return list_of_dir

