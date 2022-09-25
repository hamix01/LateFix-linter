#functions collection

def addTaps(line):
    # if tap in line? else tap
    if line[0] == "\t":
        return line
    else:
        return "\t" + line

def breakUpSentences(line, newLine = "\n"):
    signs = [":", ";", ",", ".", "!", "?"]
    for i in signs:
        if i in line:
            index = line.index(i)
            if line[index+1:index+3] != newLine[:1] and i+i != line[-3: -1]:
                line = line.replace(i, i + newLine)
    return line

def addNewLines(line, number = 0):
    return (number * "\n") + line


def checkStatement(statement):
    return statement

# def tabForBlocks(file, betterGitSupport, lineBreakSize):
#     adjustedText = "" 

#     for line in file:
#         if "begin{" in line and "document" not in line or stack != "":
#             stack = line
#         if "begin{" not in line and "end{" not in line:
#             line = addTaps(line)
#             if checkStatement(betterGitSupport):
#                 adjustedText += breakUpSentences(line, "\n\t")
#             else:
#                 adjustedText += line
#         else:
#             adjustedText += line
#         if "end{" in line:
#             stack = ""
#     return

def logic(file, betterGitSupport, lineBreakSize):
    
    adjustedText = "" 
    stack = ""
    lines = 0


    for line in file:
        if "begin{" in line and "document" not in line or stack != "":
            stack = line
            if "begin{" not in line and "end{" not in line:
                line = addTaps(line)
                if checkStatement(betterGitSupport):
                    adjustedText += breakUpSentences(line, "\n\t")
                else:
                    adjustedText += line
            else:
                adjustedText += line
            if "end{" in line:
                stack = ""

    
    if checkStatement(betterGitSupport) and "\\" != line[0] and "%" != line[0] and line != "\n":
        adjustedText += breakUpSentences(line, "\n")

    elif "%" == line[0]:
        adjustedText += line.replace("%", "% ")

    elif "\\" == line[0] and lines < lineBreakSize:
        n = len(adjustedText)
        for i in range(0, len(adjustedText)):
            if adjustedText[-1-i:n] == "\n":
                lines += 1
                n -= 1
            else:
                break

        if lines-1 < lineBreakSize:
            adjustedText += addNewLines(line, (lineBreakSize))
        elif lines-1 > lineBreakSize:
            endIndex = len(adjustedText) - (lines-1 - lineBreakSize)
            adjustedText = adjustedText[:endIndex]
            adjustedText += line
        else:
            adjustedText += line
        lines = 0

    else:
        adjustedText += line

    file.close()
    return adjustedText
