import json

with open('1.json', encoding='utf-8') as f1:
    data = json.load(f1)

for e in data:
    for k, v in e.items():
        print(k, '---', v)


def checkList2(newList):
    for i in newList:
        if type(i) == dict:
            checkDict2(i)
        elif type(i) == list:
            checkList2(i)


def checkDict2(newDict):
    for k, v in newDict.items():
        if type(v) == list:
            checkList2(v)
        else:
            if(k == 'matchInfo'):
                print('\n\n\t\t---------new game----------\n\n')
            print(k, ' --- ', v)


with open('1.json', encoding='utf-8') as f2:
    data = json.load(f2)


checkList2(data)



print('\n\n\t\t-------------------\n\n')