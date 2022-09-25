#functions collection

def printFlags():
    # print the flags that are set

    print("""
    Usages: python3 main.py [source file] [destination file (optional)] [flags]
    
    The following flags are set:
    
    --betterGitSupport      Gives a better git support
    --lineBreakSize         Sets the line break size
    """)


def addTaps(line):
    # if tap in line? else tap
    if line[0] == "\t":
        return line
    else:
        return "\t" + line


def gitSupport(line, newLine = "\n"):
    signs = [":", ";", ",", ".", "!", "?"]
    for i in signs:
        if i in line:
            index = line.index(i)
            if line[index+1:index+3] != newLine[:1] and i+i != line[-3: -1]:
                line = line.replace(i, i + newLine)
    return line


def addNewLines(line, number = 0):
    return (number * "\n") + line


def addSpace(word):
    return " " + word

def isTex(file):
    # check if the file is a tex file
    if ".tex" in file:
        return True
    else:
        return False
    

def listBlock(file, betterGitSupport=False):
    adjustedText = ""

    for line in file:

        if "begin{" not in line and "\end{" not in line:
            line = addTaps(line)
            if betterGitSupport:
                adjustedText += gitSupport(line, "\n\t")
            else:
                adjustedText += line
        else:
            adjustedText += line
        if "\end{" in line:
            break
    
    return adjustedText





def logic(file, betterGitSupport, lineBreakSize):

    adjustedText = ""

    for line in file:
        if "begin{" in line:
            adjustedText += listBlock(file, betterGitSupport)
        elif "%" in line[0]:
            # if there is no space after the %
            if line[1] != " ":
                adjustedText = adjustedText.replace(line, "") # we remove the original line
                adjustedText += line.replace("%", "% ") 
        elif lineBreakSize != 0:
            adjustedText += addNewLines(line, lineBreakSize)

    if betterGitSupport:
        adjustedText = gitSupport(adjustedText, "\n")
    
    file.close()
    return adjustedText
        
