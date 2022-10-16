import sys
import json
import pages.functions as functions

def getData():
    # get args
    args = sys.argv

    
    jsonFile = open("config.json")
    jsonData = json.load(jsonFile)
    lineBreakSize = jsonData["lineBreakSize"]
    betterGitSupport = jsonData["betterGitSupport"]

    if(len(args) > 1):
        if(args[1] == "--help" or args[1] == "-h"):
            functions.printFlags()
            return
    else:
        functions.printFlags()
        return

    for i in args:
        if "--betterGitSupport" in i:
            betterGitSupport = True
        if "--lineBreakSize" in i:
            lineBreakSize = int(args[args.index(i) + 1])

    print("Better git support: " + str(betterGitSupport))
    print("Line break size: " + str(lineBreakSize))

    filePath = args[1]
    if functions.isTex(filePath):
        functions.logic(filePath, betterGitSupport, lineBreakSize)
    else:
        print("The file is not a tex file")



def main():
    getData()

if __name__ == "__main__":
    main()




# import argparse

# parser = argparse.ArgumentParser(description="Better git support and Line break size")
# parser.add_argument("file", type=str, help="The file to be formatted")
# parser.add_argument("betterGitSupport", type=bool, help="Better git support")
# parser.add_argument("LineBreakSize", type=int, help="Decide the line break size")

# args = parser.parse_args()


########## NEW CODE IN MAIN ##########
    # args = parser.parse_args()
    # print(args)
    # print(args.file)
    # print(args.betterGitSupport)
    # print(args.LineBreakSize)
    # jsonFile = open("config.json")
    # jsonData = json.load(jsonFile)

    # print("Better git support: " + str(args.betterGitSupport))
    # print("Line break size: " + str(args.LineBreakSize))
    # if functions.isTex(args.file):
    #     functions.logic(args.file, args.betterGitSupport, args.LineBreakSize)
    # else:
    #     print("The file is not a tex file")