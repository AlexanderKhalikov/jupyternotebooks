import json
from pprint import pprint

with open('1.json', encoding='utf-8') as f1:
    data = json.load(f1)

for e in data:
    for k, v in e.items():
        print(k, '---', v)


print('\n\n\n\n')


with open('2.json', encoding='utf-8') as f2:
    data = json.load(f2)

for k, v in data.items():
    print(k, '---', v)


events = data['events']
print(type(events))
print('\n\n\n\n')

for i in events:
    markets = i['markets']
    for market in markets:
        for row in market['rows']:
            for k, v in row.items():
                print(type(v))
                print(k, '---', v)
            print('\n\t\t-------------------')
        # for k, v in i.market():
        #     print(k, '---', v)
    break

printCount = 0

def checkList1(newList):
    for i in newList:
        if type(i) == dict:
            checkDict1(i)
        elif type(i) == list:
            checkList1(i)


def checkDict1(newDict):
    global printCount
    # if printCount > 200:
    #     return
    for k, v in newDict.items():
        if type(v) == list:
            checkList1(v)
        else:
            if (k == 'eventName' or k == 'value' or k == 'cartQuoteName'):
                if (k == 'eventName'):
                    print('\n\n\t\t---------new game----------\n\n')
                print(k, ' --- ', v)
                printCount += 1



print('\n\n\t\t-------------------\n\n')


for event in data['events']:
    checkDict1(event)
    # break


print('\n\n\t\t-------------------\n\n')


# def checkList2(newList):
#     for i in newList:
#         if type(i) == dict:
#             checkDict2(i)
#         elif type(i) == list:
#             checkList2(i)
#
#
# def checkDict2(newDict):
#     for k, v in newDict.items():
#         if type(v) == list:
#             checkList2(v)
#         else:
#             print(k, ' --- ', v)
#
#
# with open('1.json', encoding='utf-8') as f2:
#     data = json.load(f2)
#
#
# checkList2(data)
#
#
#
# print('\n\n\t\t-------------------\n\n')
#
#
# def checkList3(newList):
#     for i in newList:
#         if type(i) == dict:
#             checkDict3(i)
#         elif type(i) == list:
#             checkList3(i)
#
#
# def checkDict3(newDict):
#     for k, v in newDict.items():
#         if type(v) == list:
#             checkList3(v)
#         else:
#             print(k, ' --- ', v)
#
#
# with open('3.json', encoding='utf-8') as f2:
#     data = json.load(f2)
#
#
# checkDict3(data)
