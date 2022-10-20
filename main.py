"""
This is the main file
"""
import argparse
import json
from pages import functions

parser = argparse.ArgumentParser(description="Better git support and Line break size")
# parser.add_argument("better_git_support", type=bool, help="Better git support")
# parser.add_argument("line_break_size", type=int, help="Decide the line break size")
parser.add_argument("file", type=str, help="The file to be formatted")
parser.add_argument("-b", "--better_git_support", help="Better git support")
parser.add_argument("-l", "--line_break_size", help="Decide the line break size", type=int)

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
            print("Invalid value for better_git_support")
            return

    if args.line_break_size:
        line_break_size = args.line_break_size


    if functions.is_tex(args.file):
        print("Line break size: " + str(line_break_size))
        print("Better git support: " + str(better_git_support))
        functions.logic(args.file, better_git_support, line_break_size)
    else:
        print("The file is not a tex file")





    #     args = sys.argv
    #     # json_file = open("config.json")
    # json_data = json.load(json_file)
    # line_break_size = json_data["line_break_size"]
    # better_git_support = json_data["better_git_support"]

    # if(len(args) > 1):
    #     if(args[1] == "--help" or args[1] == "-h"):
    #         functions.printFlags()
    #         return
    # else:
    #     functions.printFlags()
    #     return

    # for i in args:
    #     if "--better_git_support" in i:
    #         better_git_support = True
    #     if "--line_break_size" in i:
    #         line_break_size = int(args[args.index(i) + 1])

    # print("Better git support: " + str(better_git_support))
    # print("Line break size: " + str(line_break_size))

    # filePath = args[1]
    # if functions.isTex(filePath):
    #     functions.logic(filePath, better_git_support, line_break_size)
    # else:
    #     print("The file is not a tex file")
