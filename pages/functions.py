#functions collection

from ast import operator


def printFlags():
    # print the flags that are set

    print("""
    Usages: python3 main.py [source file] [flags]
    
    The following flags are set:
    
    --betterGitSupport      Gives a better git support
    --lineBreakSize         Sets the line break size
    """)

def isTex(file): # check if the file is a tex file
    isTex = False
    if ".tex" in file:
        isTex = True
    return isTex

def getText(filePath):
    text = ""
    file = open(filePath, "r")
    for line in file:
        text += line
    file.close()
    return text

def addTaps(line): # add taps to the line
    return "\t" + line

def addLines(text, number):
    # finalText = ""
    # for line in text.split("\n"):
    #     line = (number * "\n") + line
    #     finalText += line 
    # print(finalText)
    # for line in text.strip():
    #     print(line + ">12312>s123213hell")

    return number

def removeLines(text, lineBreakSize):

    finalText = ""
    # text = text.replace('\n','')

    # finalText = addLines(text, lineBreakSize)
    for line in text:
        # finalText += line.strip()
        print(line.split("\n"))
    # print(finalText)

    return finalText


def makeNewFile(text, name):
    newFile = open(name, "w")
    newFile.write(text)
    newFile.close()
    fileDone = "File " + name + " created"
    return fileDone


def spaceAfterComment(text):
    finalText = ""
    for line in text.split("\n"):
        if containWord("%", line):
            line = line.replace("%", " % ")
        finalText += line + "\n"
    return finalText

def containWord(word, string): # check if a word is in a string
    contains = False
    if word in string:
        contains =  True
    return contains

def chooseFileName():
    fileName = input("Enter the file name: ") + ".tex"
    return fileName

def TabList(text):
    finalText = ""
    isList = False

    for line in text.split("\n"):
        if containWord("begin{", line) and not(containWord("document", line)) and not(containWord("%\begin", line)):
            finalText += line + "\n"
            isList = True
            continue
        elif isList:
            if containWord("end{", line) and not(containWord("document", line)) and not(containWord("%\end", line)):
                finalText += line + "\n"
                isList = False
                continue
            else:
                finalText += addTaps(line) + "\n"
        else:
            finalText += line + "\n"
    return finalText

def addNewLine(text):
    finalText = ""
    marks = [":", ";", ",", ".", "!", "?"]
    for line in text.split("\n"):
        for mark in marks:
            if mark in line:
                line = line.replace(mark, mark + "\n")
        finalText += line + "\n"
    return finalText


def mathMode(text):
#space after math mode
    signs = ["+", "-", "*", "/", "=", "(", ")", "[", "]", "{", "}", ">", "<", "!", "|", "&", "^", "~", ":", ";", ",", ".", "!", "?", "$"]
    finalText = ""
    for line in text.split("\n"):
        if containWord("$", line):
            for sign in signs:
                if sign in line:
                    line = line.replace(sign, " " + sign + " ")
        finalText += line + "\n"
    return finalText

def logic(filePath, betterGitSupport, lineBreakSize):
    text = getText(filePath)
    # finalText = ""

    if betterGitSupport:
        text = addNewLine(text)

    if "begin{" in text:
        text = TabList(text)
    
    text = spaceAfterComment(text)
    text = mathMode(text)
    
    if lineBreakSize > 0:
        text = removeLines(text, lineBreakSize)
        # text = addLines(text, lineBreakSize)

    # fileName = chooseFileName()
    # fileDone = makeNewFile(finalText, fileName)
    print(text)
    return text
