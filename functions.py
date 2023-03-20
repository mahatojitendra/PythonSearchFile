import os

def searchfile(dir):
    if os.path.isfile(dir):
        print('File: {}'.format(dir))
    elif os.path.isdir(dir):
        paths = os.listdir(dir)
        for path in paths:
            path = dir + '\\' + path
            searchfile(path)
    else:
        print('Error: Something went wrong.')