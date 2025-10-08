
from argparse import ArgumentParser
from An0nMethods import *


def main():
    anon = An0n()
    parser = ArgumentParser(description="Secure file and directory deletion tool")

    parser.add_argument("-f", "--file", help="Path to file for secure deletion")
    parser.add_argument("-d", "--dir", help="Path to directory for secure deletion")
    parser.add_argument("-p", "--passes", type=int, default=3,
                        help="Number of overwrite passes (default: 3)")

    args = parser.parse_args()
    file = args.file
    dir = args.dir
    passes = args.passes

    # Check if no arguments provided
    if not any([file, dir]):
        parser.print_help()
        print("\nError: You must specify either -f/--file or -d/--dir")
        exit(1)

    # Process directory
    if dir:
        if anon.isDir(dir):
            print(f"Securely deleting directory: {dir} (passes: {passes})")
            anon.deleteDir(dir, passes)
            print(f"Directory {dir} successfully deleted")
        else:
            print(f"Error: {dir} is not a directory or does not exist.")
            exit(1)

    # Process file
    if file:
        if anon.isFile(file):
            print(f"Securely deleting file: {file} (passes: {passes})")
            anon.deleteFile(file, passes)
            print(f"File {file} successfully deleted")
        else:
            print(f"Error: {file} is not a file or does not exist.")
            exit(1)


if __name__ == "__main__":
    main()