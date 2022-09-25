import sys
import json
import pages.welcome as welcome
import pages.menu as menu
# from pages import functions





# linter



def main():
    jsonFile = open("config.json")
    jsonData = json.load(jsonFile)
    # lineBreakSize = jsonData["lineBreakSize"]
    # betterGitSupport = jsonData["betterGitSupport"]

    # file = open( "hello.tex")
    getInput = input(">> ")
    print(welcome, getInput)
    if getInput == "menu":
        print(menu)
    elif getInput == "exit" or "q":
        print("Bye, bye - Have a nice day!")
    else:
        print("That is not a valid choice. You can only choose from the menu.")
        input("\nPress enter to continue...")


    

    

    #print(functions.process(file, betterGitSupport, lineBreakSize))
    # # while (True):
    # #     print(menu)



    # #     args = input(">> ")
    # #     print(args)

    # #     if args == "q":
    # #         print("Bye, bye - I hope you got help!")
    # #         break
    # #     else:
    # #         print("That is not a valid choice. You can only choose from the menu.")
    # #     input("\nPress enter to continue...")



# #args = sys.argv
    # # args = ['main.py', 'hello.tex', 'betterGitSupport:', 'True']
    # # f = open( "hello.tex")#args[1])
    # # print(args)

    # # if len(args) == 2:
    # #     betterGitSupport = jsonData["betterGitSupport"]
    # #     lineBreakSize = jsonData["lineBreakSize"]
    # # elif len(args) == 3:
    # #     if "git" in args[2] and args[2] == "True":
    # #         betterGitSupport = True
    # #         lineBreakSize = jsonData["lineBreakSize"]

    # #     elif "line" in args[2]:
    # #         lineBreakSize = args[3]
    # #         betterGitSupport = jsonData["betterGitSupport"]
    # # elif len(args) == 5:
    # #     betterGitSupport = args[3]
    # #     lineBreakSize = args[5]
        


if __name__ == "__main__":
    main()