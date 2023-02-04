import ast
import argparse

def argumentsParse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", help="word to generate the leetspeak for")
    parser.add_argument("-o", "--outputFile", help="Output filename")
    parser.add_argument("-l", "--level", help="Specify the aggressiveness of the list", type=int)
    args = parser.parse_args()
    return args

def varInits():
    args = argumentsParse()
    strInput = args.word.upper()
    stringLength = len(strInput)
    outputFile = args.outputFile if args.outputFile else 'wordlist'
    level = args.level
    return [strInput, stringLength, outputFile, level]

def listSelect(level):
    fileList = ['leetspeakListSmall', 'leetspeakList']
    with open('Lists/' + fileList[level], 'r', encoding="utf8") as fl:
        data = fl.read()
    dct = ast.literal_eval(data)
    return dct

def leetSpeakGen(index=0):
    alphaList = dct[strInput[index]]
    for character in alphaList:
        stackList.append(character)
        if(index == stringLength - 1):
            file.write(''.join(map(str, stackList)) + '\n')
        else:
            leetSpeakGen(index+1)
        stackList.pop()

strInput, stringLength, outputFile, level = varInits()
dct = listSelect(level=0)
stackList = []
with open(outputFile, 'w+', encoding="utf8") as file:
    leetSpeakGen()  
print(f'Wordlist generated and stored in {outputFile}')
