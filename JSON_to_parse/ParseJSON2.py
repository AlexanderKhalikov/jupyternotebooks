import json

with open('2.json', encoding='utf-8') as f2:
    data = json.load(f2)

# for k, v in data.items():
#     print(k, '---', v)
#
#
# events = data['events']
# print(type(events))
# print('\n\n\n\n')
#
# for i in events:
#     markets = i['markets']
#     for market in markets:
#         for row in market['rows']:
#             for k, v in row.items():
#                 print(type(v))
#                 print(k, '---', v)
#             print('\n\t\t-------------------')
#         # for k, v in i.market():
#         #     print(k, '---', v)
#     break
#
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



for event in data['events']:
    checkDict1(event)
    # break


print('\n\n\t\t-------------------\n\n')
