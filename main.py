# python script to find and replace a word from files under folders
from functions import searchfile, os

filepath = input('Please enter the path = ')

if filepath[len(filepath) - 1] == '/':
    pass
elif filepath[len(filepath) - 1] == '\\':
    pass
else:
    filepath = filepath + '\\'

try:
    paths = os.listdir(filepath)
except:
    print ('Something is wrong with input: {}'.format(filepath))
else:
    for path in paths:
        path = filepath + path
        searchfile(path)