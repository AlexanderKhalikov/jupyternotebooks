import json

def checkList3(newList):
    for i in newList:
        if type(i) == dict:
            checkDict3(i)
        elif type(i) == list:
            checkList3(i)


def checkDict3(newDict):
    for k, v in newDict.items():
        if type(v) == list:
            checkList3(v)
        else:
            print(k, ' --- ', v)


with open('3.json', encoding='utf-8') as f2:
    data = json.load(f2)


checkDict3(data)