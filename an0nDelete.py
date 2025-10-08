import sys
from argparse import ArgumentParser
from An0nMethods import *


anon = An0n()
parser = ArgumentParser()
parser.add_argument("-f", "--file")
parser.add_argument("-d", "--dir")
parser.add_argument("-p", "--passes", type=int)


args = parser.parse_args()
file = args.file
dir = args.dir
passes = args.passes



if dir:
    if anon.isDir(dir):
        anon.deleteDir(dir, passes) if passes is not None else anon.deleteDir(dir)
    else:
        print(f"{dir} is not a directory.")
        exit(0)
if file:
    if anon.isFile(file):
        anon.deleteFile(file, passes) if passes is not None else anon.deleteFile(file)
    else:
        print(f"{file} is not a file.")
        exit(0)



