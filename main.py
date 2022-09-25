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
        file = open(filePath, "r")
        print(functions.logic(file, betterGitSupport, lineBreakSize))
    else:
        print("The file is not a tex file")



def main():
    getData()



if __name__ == "__main__":
    main()