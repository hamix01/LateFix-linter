import sys
import json

from pages.functions import logic
    # from pages import functions

def printFlags():
    # print the flags that are set

    print("""
    Usages: python3 main.py [source file] [destination file (optional)] [flags]
    
    The following flags are set:
    
    --betterGitSupport      Gives a better git support
    --lineBreakSize         Sets the line break size
    """)

def getData():
    # get args
    args = sys.argv
    
    jsonFile = open("config.json")
    jsonData = json.load(jsonFile)
    lineBreakSize = jsonData["lineBreakSize"]
    betterGitSupport = jsonData["betterGitSupport"]

    if(len(args) > 1):
        if(args[1] == "--help" or args[1] == "-h"):
            printFlags()
            return
    else:
        printFlags()
        return

    for i in args:
        if "--betterGitSupport" in i:
            betterGitSupport = True
        if "--lineBreakSize" in i:
            lineBreakSize = args[args.index(i) + 1]

    print("Line break size: " + str(lineBreakSize))

    filePath = args[1]
    file = open(filePath, "r")

    print(logic(file, betterGitSupport, lineBreakSize))

def main():
    getData()



if __name__ == "__main__":
    main()