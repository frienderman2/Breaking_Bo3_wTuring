# Callaghan Donnelly
# the file with the overall main function and setup functions
# TODO: iterate all 'th' plaintext replacement bigrammes
# TODO: Implement either a dicitonary search or NLP to shave down on the saved responses (Sidenote - NOT doing NLP, wayyyyyy too much work, and quite divergent from the original intent of this program)
# TODO: if that all fails, try checking ALL bigrammes in the cypher text as th and see what happens
# TODO: multiprocess so that I can just brute force the damn thing if all of my half-baked math falls through (which would not suprise me)
# TODO: if all of that still fails, then this is not a typical bigramme cypher OR exlude p from the alphabet (as p apparently NEVER appears)
# Also the basic assumption (and possible flaw) is that I am dealing with a single shift bigramme cypher, if it is even a rotating shift, or something more complex, then this whole process is useless
# TODO: if all the single shift operations fail, try something akin to Turing's solving of the Vingette in 'The Application of Probability to Cryptogrophy' ... keyword try b/c I can only understang 1/2 of the math presented

import Simple_Shift
from Simple_Shift import *


# setup the cypher text into lists for manipulation
def setLists(cyphtxt):
    cyphList = cyphtxt.split()
    firstLetterList = []
    secondLetterList = []
    # pull each letter category into its own list
    for bigramme in cyphList:
        firstLetterList.append(bigramme[0])
        secondLetterList.append(bigramme[1])

    # now put those in a list to return
    return [firstLetterList, secondLetterList]


# unused function to gather basic info on the letter/bigramme stats
def getFrequencies():
    cyphtxt = 'bx re yh zy bf lm kt ut yg se tb sx ky co jh km aq ve tx vx cy ji ut vt kn vc gx aw ij av qn lg ef fj uq bd kn sv ' \
              'cx fn je vr rk kn cg aw xq vn zf li fh vz wt ta ia ij zf eh uf tj qm yg hl yq cx ij vw ig de qz tg nj rs er vk tm sa ' \
              'yv tw hr hs lt vy kr qc tv gh hb jn yb qh er ut gk et cs wv jl rh xo wr ex hr xt zi kc xs qs fd wd cm ku ah fh fj ' \
              'lf ui ly sh vf au xm hx qw dl gi cx vb dh wt xm kv un ej kt kt ye cg jd ef eh zv xt he uz tg cl jw nr tw ur vo jt ' \
              'jo ru iq iy rz ey ho gd nq yn bq ul ai fh bu ji ho nw qg yg vj if yv zu id jc gh ke xr qf cq ra it gw dl fc gq yi iu ' \
              'qu ny vr gy sj rh iu hi wr mv ym zi lk re vk xu ry uq gs ve qd yn bq ch ky er qh jr ho ya ek ky zj ei hz cb if dk'

    bigrams = ['th', 'he', 'in', 'er', 'an', 're', 'nd', 'on', 'en', 'at', 'ou', 'ed', 'ha', 'to', 'or', 'it', 'is',
               'hi', 'es', 'ng']
    possibleTH = ['kt', 'ut', 'kn', 'ij', 'cx']

    cyphList = cyphtxt.split()
    print(len(cyphList))
    countDict = {}

    for bigram in cyphList:
        # if 'p' in bigram:
        #     print(bigram + "HERE")
        try:
            countDict[bigram] = countDict[bigram] + 1

        except KeyError as e:
            countDict[bigram] = 1

    keyList = countDict.keys()
    for key in countDict:
        if countDict[key] > 2:
            print(key + ',' + str(countDict[key]))

    # print(keyList)

    print(countDict)


# change all of the letters in given list by difference between letters in first list and comparison character
def doDiffs(possibilityList, compareToChar, largeCharList):
    # have a list to hold all of the new permutations of 'fixed' character lists
    finalList = []
    for possibles in possibilityList:
        mover = findMove(possibles, compareToChar)
        fixedList = ShiftCharList(largeCharList, mover)
        finalList.append(fixedList)

    return finalList


# merge two character lists in alternating order (using some super cool slicing trick I just learned)
def mergeCharLists(startList1, startList2):
    returnList = [None] * (len(startList1) + len(startList2))
    returnList[::2] = startList1
    returnList[1::2] = startList2
    return returnList


if __name__ == '__main__':
    cyphtxt = 'bx re yh zy bf lm kt ut yg se tb sx ky co jh km aq ve tx vx cy ji ut vt kn vc gx aw ij av qn lg ef fj uq bd kn sv ' \
              'cx fn je vr rk kn cg aw xq vn zf li fh vz wt ta ia ij zf eh uf tj qm yg hl yq cx ij vw ig de qz tg nj rs er vk tm sa ' \
              'yv tw hr hs lt vy kr qc tv gh hb jn yb qh er ut gk et cs wv jl rh xo wr ex hr xt zi kc xs qs fd wd cm ku ah fh fj ' \
              'lf ui ly sh vf au xm hx qw dl gi cx vb dh wt xm kv un ej kt kt ye cg jd ef eh zv xt he uz tg cl jw nr tw ur vo jt ' \
              'jo ru iq iy rz ey ho gd nq yn bq ul ai fh bu ji ho nw qg yg vj if yv zu id jc gh ke xr qf cq ra it gw dl fc gq yi iu ' \
              'qu ny vr gy sj rh iu hi wr mv ym zi lk re vk xu ry uq gs ve qd yn bq ch ky er qh jr ho ya ek ky zj ei hz cb if dk'

    # the 20 most common bigrammes in the english language
    bigrams = ['th', 'he', 'in', 'er', 'an', 're', 'nd', 'on', 'en', 'at', 'ou', 'ed', 'ha', 'to', 'or', 'it', 'is',
               'hi', 'es', 'ng']
    # I'm working on the mathematical assumption that one of these 10 HAS to be 'th' so for simplicity sake, I'm only swapping for 't' and 'h'
    theTVar = 't'
    theHVar = 'h'
    # all the possible bigrammes in the cypher text that could be 'th'
    possibleTH = ['kt', 'ut', 'kn', 'ij', 'cx', 'yg', 'ky', 'fh', 'er', 'ho']
    # first letter list
    poss1 = ['k', 'u', 'k', 'i', 'c', 'y', 'k', 'f', 'e', 'h', 'o']
    # second letter list
    poss2 = ['t', 't', 'n', 'j', 'x', 'g', 'y', 'h', 'r', 'o', 'o']

    # get the two separated sets of letters (the first of each bigramme in one and the second in the other)
    charLists = setLists(cyphtxt)
    firstList = charLists[0]
    secondList = charLists[1]

    # brute force every possible swap
    poss1 = poss1 + firstList
    poss2 = poss2 + secondList

    bigrammeAsString = ''.join(bigrams)
    bigrammeFormatted = ' '.join(bigrammeAsString[i:i + 2] for i in range(0, len(bigrammeAsString), 2))
    bigrammeList = setLists(bigrammeFormatted)
    tList = bigrammeList[0]
    hList = bigrammeList[1]

    # do all the movement and get back two sets of character lists to be sequentially merged
    characterSet1 = []
    characterSet2 = []
    # this is a rough brute force at this point, but I'm starting to think it might not be a single shift bigramme
    for i in range(len(tList)):
        theTVar = tList[i]
        theHVar = hList[i]
        tempSet1 = doDiffs(poss1, theTVar, firstList)
        tempSet2 = doDiffs(poss2, theHVar, secondList)
        characterSet1.extend(tempSet1)
        characterSet2.extend(tempSet2)

    print(len(characterSet1))

    # sequentially merge and output results
    for i in range(len(characterSet1)):
        outputs = mergeCharLists(characterSet1[i], characterSet2[i])
        cleanStr = ''.join(outputs)
        if 'the' in cleanStr:
            print(f"-------------------Output Attempt #{i + 1}-------------------")
            # biStr = ' '.join(cleanStr[i:i + 2] for i in range(0, len(cleanStr), 2))
            print(cleanStr)
            print('\n')
