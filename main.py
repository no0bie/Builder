import os, sys

allowedColors = ["purple(", "blue(", "green(", "yellow(", "red(", "bold(", "underline("]
defVariables = {}
defFunctions = {}

funBuilderCheck = 0
currFunction = ""

#TODO add colour support
class bcolors:

    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def errMsg(notFound, nameOf):
    print(bcolors.red + bcolors.bold + "ERROR: No " + notFound + " with the name '" + nameOf + "'" + bcolors.end,end='')

def readCode(fileLocation):
    syntaxF = open(fileLocation, "r")
    allSyntax = syntaxF.readlines()
    syntaxF.close()
    for syntax in allSyntax:
        proccessSyntax(syntax.replace('\n', ''))

def returnVariable(checkVariables):
    for checkVariable in checkVariables.split(' '):
        if checkVariable.startswith("VAR("):
            toRemove = checkVariable.replace("VAR(", "").replace(")", "")
            if toRemove in defVariables.keys():
                checkVariables = checkVariables.replace("VAR(" + toRemove + ")", defVariables[toRemove])
                return checkVariables
            else:
                errMsg("variable", toRemove)
                return ""

def doesVarExist(line):
    return "VAR(" in line

def funBuilder(syntaxInFunction):
    defFunctions[currFunction].append(syntaxInFunction)

def proccessSyntax(proccessed):
    global funBuilderCheck, currFunction

    if proccessed.startswith("#"):
        pass

    elif proccessed.startswith("DEF "):
        currFunction = proccessed.replace("DEF ", "")
        defFunctions[currFunction] = []
        funBuilderCheck = 1

    elif proccessed.startswith("END"):
        funBuilderCheck = 0
        currFunction = ""

    elif funBuilderCheck == 1:
        funBuilder(proccessed)

    elif proccessed.startswith("CALL "):
        if proccessed.replace("CALL ", "") in defFunctions.keys():
            for functionCode in defFunctions[proccessed.replace("CALL ", "")]:
                proccessSyntax(functionCode)
        else:
            errMsg("function", proccessed.replace("CALL ", ""))
            print()

    elif proccessed.startswith("PRINT "):
        if doesVarExist(proccessed.replace('PRINT ', '')):
            print(returnVariable(proccessed.replace('PRINT ', '')))
        else:
            print(proccessed.replace('PRINT ', ''))

    elif proccessed.startswith("COM "):
        if doesVarExist(proccessed.replace('COM ', '')):
            os.system(returnVariable(proccessed.replace('COM ', '')))
        else:
            os.system(proccessed.replace('COM ', ''))

    elif proccessed.startswith("VAR "):

        defVariables[proccessed.replace('VAR ', '').split(" ")[0]] = proccessed.replace('VAR ', '').replace(proccessed.replace('VAR ', '').split(" ")[0] + " ", "")

    elif proccessed.startswith("NEWLINE"):
        print()

try:
    fileSpecified = sys.argv[1]
except:
    print("Especify file to build")

readCode(fileSpecified)
