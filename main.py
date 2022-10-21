"""
This is the main file for the LateFix project
"""
import argparse
import json
from pages import functions

parser = argparse.ArgumentParser(description="Better git support and Line break size")
parser.add_argument("file", type=str, help="The file to be formatted")
parser.add_argument("-git", "--better_git_support", help="Better git support")
parser.add_argument("-line", "--line_break_size", help="Decide the line break size", type=int)

args = parser.parse_args()


def main():
    """
        Get arguments from the command line or the config file
    """

    json_file = open("config.json", encoding="utf-8")
    json_data = json.load(json_file)

    better_git_support = json_data["better_git_support"]
    line_break_size = int(json_data["line_break_size"])

    if args.better_git_support:
        if args.better_git_support == "True":
            better_git_support = True
        elif args.better_git_support == "False":
            better_git_support = False
        else:
            print("Invalid value")
            return

    if args.line_break_size:
        line_break_size = args.line_break_size


    if functions.is_tex(args.file):
        print("LateFix Linter...")
        print("Line break size: " + str(line_break_size))
        print("Better git support: " + str(better_git_support))
        functions.logic(args.file, better_git_support, line_break_size)
    else:
        print("The file is not a tex file")


if __name__ == "__main__":
    main()
