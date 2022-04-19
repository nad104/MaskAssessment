import os

def make_dir(foldername):
    directory = foldername
    parent_dir = "D:\Documents\Flickr Faces"

    # Create if it does not already exist
    mode = 0o666

    path = os.path.join(parent_dir, directory)

    os.makedirs(path, mode)
    print("Directory '% s' created" % directory)