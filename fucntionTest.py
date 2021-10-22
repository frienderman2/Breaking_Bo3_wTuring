# file for ensuring individual functions work correctly

def funcTest(startList1, startList2):
    returnList = [None] * (len(startList1) + len(startList2))
    returnList[::2] = startList1
    returnList[1::2] = startList2
    return returnList




def newShiftCharList(ogList, movement):
    # for each character, add to its ASCII value and place the new char in the new list
    newlist = []
    for char in ogList:
        newChar = chr((ord(char) + movement - 97) % 26 + 97)
        newlist.append(newChar)

    # return the modified list
    return newlist


def testDriver():
    cyphtxt = 'vb km km ei qf kw ch fy ei fy ai wl dc vw ju um es rb gl vl gs cl eb'
    poss1 = ['v']
    poss2 = ['b']



def main():
    list1 = ['T', 'i', ' ', 's', 'c', 'o']
    list2 = ['h', 's', 'i', ' ', 'o', 'l']

    sentence = 'this is cool i can decode your bitch ass cypher treyarch'
    split1 = ['t', 'i', 'i', 'c', 'o', 'i', 'a', 'd', 'c', 'd', 'y', 'u', 'b', 't', 'h', 's', 'c', 'p', 'e', 't', 'e', 'a', 'c']
    split2 = ['h', 's', 's', 'o', 'l', 'c', 'n', 'e', 'o', 'e', 'o', 'r', 'i', 'c', 'a', 's', 'y', 'h', 'r', 'r', 'y', 'r', 'h']
    thing1 = 'tiicoiadcdyubthscpeteac'
    thing2 = 'hssolcneoeoricasyhrryrh'

    ceasar1 = 'vkkeqkcfefawdvjuergvgce'
    ceasar2 = 'bmmifwhyiyilcwumsbllslb'
    split1 = list(ceasar1)
    split2 = list(ceasar2)
    fin = funcTest(split1, split2)
    print(fin)
    encodedText = ''.join(fin)
    print(encodedText)
    bigramCyph = 'vb km km ei qf kw ch fy ei fy ai wl dc vw ju um es rb gl vl gs cl eb'


main()
