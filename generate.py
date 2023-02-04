import ast
strInput = "demoString"
strInput = strInput.upper()


stringLength = len(strInput)

with open("leetspeakListSmall", 'r', encoding="utf8") as fl:
    data = fl.read()
dct = ast.literal_eval(data)

stackList = []

def leetSpeakGen(index=0):
    alphaList = dct[strInput[index]]
    for character in alphaList:
        stackList.append(character)
        if(index == stringLength - 1):
            print(''.join(map(str, stackList)))
        else:
            leetSpeakGen(index+1)
        stackList.pop()


leetSpeakGen()