# Callaghan Donnelly
# Simple ceasar shift of full alphabet

# find the integer difference between two chars
def findMove(cypherChar, assumedChar):
    cyphInt = ord(cypherChar)
    assInt = ord(assumedChar)

    # find diff from 'a' (97)
    cyphDiff = cyphInt - 97
    assDiff = assInt - 97

    # find diff between those two
    toMove = cyphDiff - assDiff

    # find the correct direction to move
    toMove = toMove * -1

    return toMove

# shifts all chars in a given list by a given amount
def ShiftCharList(ogList, movement):
    # for each character, add to its ASCII value and place the new char in the new list
    newlist = []
    for char in ogList:
        newChar = chr((ord(char) + movement - 97) % 26 + 97)
        newlist.append(newChar)

    # return the modified list
    return newlist
