#functions collection

def printFlags():
    # print the flags that are set

    print("""
    Usages: python3 main.py [source file] [destination file (optional)] [flags]
    
    The following flags are set:
    
    --betterGitSupport      Gives a better git support
    --lineBreakSize         Sets the line break size
    """)

def isTex(file):
    # check if the file is a tex file
    if ".tex" in file:
        return True
    else:
        return False
    
def addTaps(line):
    return "\t" + line


def addNewLine(line):
    marks = [":", ";", ",", ".", "!", "?"]
    for i in marks:
        if i in line:
            line = line.replace(i, i + "\n")
    return line


def addLines(line, number):
    return (number * "\n") + line


def addSpace(word):
    return " " + word


def SpaceAfterComment(line):
    adjustedText = ""

    if line[1] != " ":
        adjustedText = adjustedText.replace(line, "") # we remove the original line
        adjustedText += line.replace("%", "% ") # and add a space after the %

    return adjustedText


def listBlock(file, betterGitSupport=False):
    adjustedText = ""

    for line in file:

        if "begin{" not in line and "\end{" not in line:
            line = addTaps(line)

            if betterGitSupport:
                adjustedText += addNewLine(line)
                line = addTaps(line)
                 
            else:
                adjustedText += line
        else:
            adjustedText += line
        if "\end{" in line:
            # line += adjustedText
            break
    print(adjustedText)

    return adjustedText

def TapsInList(file, betterGitSupport, lineBreakSize, line):
    adjustedText = ""

    if "begin{" in line and "document" not in line:
        print(line)

        adjustedText += listBlock(file, betterGitSupport)
        
    elif "%" in line[0]:     # if there is no space after the %
        SpaceAfterComment(line)
    elif lineBreakSize != 0:
        adjustedText += addLines(line, lineBreakSize)

    return adjustedText


   

def logic(file, betterGitSupport, lineBreakSize):

    adjustedText = ""
            
    for line in file:
        adjustedText += line
        TapsInList(file, betterGitSupport, lineBreakSize, line)

    if betterGitSupport:
        for line in file:
            adjustedText += addNewLine(line)


    # for line in file:
    #     if "begin{" in line and "document" not in line:
    #         adjustedText += line
    #         adjustedText += listBlock(file, betterGitSupport)
    #     elif "%" in line[0]:
    #         # if there is no space after the %
    #         if line[1] != " ":
    #             adjustedText = adjustedText.replace(line, "") # we remove the original line
    #             adjustedText += line.replace("%", "% ") 
    #     elif lineBreakSize != 0:
    #         adjustedText += addNewLines(line, lineBreakSize)

    # if betterGitSupport:
    #     adjustedText = newSentence(adjustedText, "\n")
    
    file.close()
    return adjustedText
        