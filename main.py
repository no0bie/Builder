import os, sys

defVariables = {}

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
            checkVariables = checkVariables.replace("VAR(" + toRemove + ")", defVariables[toRemove])
    return checkVariables

def doesVarExist(line):
    return "VAR(" in line

def proccessSyntax(proccessed):
    if proccessed.startswith("#"):
        pass
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
