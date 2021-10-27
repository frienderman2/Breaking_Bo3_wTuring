# Callaghan Donnelly
# 10/26/2021
# abandoning the complex math and using modern compute power and a good old fashioned dictionary to find possible cribs/encyphering words

cyphtxt = 'bx re yh zy bf lm kt ut yg se tb sx ky co jh km aq ve tx vx cy ji ut vt kn vc gx aw ij av qn lg ef fj uq bd kn sv ' \
          'cx fn je vr rk kn cg aw xq vn zf li fh vz wt ta ia ij zf eh uf tj qm yg hl yq cx ij vw ig de qz tg nj rs er vk tm sa ' \
          'yv tw hr hs lt vy kr qc tv gh hb jn yb qh er ut gk et cs wv jl rh xo wr ex hr xt zi kc xs qs fd wd cm ku ah fh fj ' \
          'lf ui ly sh vf au xm hx qw dl gi cx vb dh wt xm kv un ej kt kt ye cg jd ef eh zv xt he uz tg cl jw nr tw ur vo jt ' \
          'jo ru iq iy rz ey ho gd nq yn bq ul ai fh bu ji ho nw qg yg vj if yv zu id jc gh ke xr qf cq ra it gw dl fc gq yi iu ' \
          'qu ny vr gy sj rh iu hi wr mv ym zi lk re vk xu ry uq gs ve qd yn bq ch ky er qh jr ho ya ek ky zj ei hz cb if dk'


# basic idea:
# STEP 1: grab just the first line of text
# STEP 2: Assume each possible set of 3 chars can be shifted to make 'the'
# STEP 3: let the amount each letter was moved represent a letter of the encryption word
# STEP 4: search whatever dictionary I have for those three letters in that order in each word, and any words that have that get saved as possible encyphering words
# TODO: get a dictionary (preferably oxford)
# STEP 5: try the possible enchiphering words and hopefully I will find some partial words here and there throughout the text
# STEP 6: if that fails or I just don't see any visibly, use that fancy math they used to see if they were getting closer to the right rotors in enigma

# find the integer difference between two chars
def findMove(cypherChar, plainChar):
    cyphInt = ord(cypherChar) - 97
    plainInt = ord(plainChar) - 97

    charIndex = cyphInt - plainInt

    return charIndex


def setChar(index):
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    try:
        return alphabetList[index]
    except IndexError as e:
        print(f"Tried to access index {index}... not sure why. Weird.")
        # FIXME
        # it only happens once in tests, so hopefully not an issue? this is gonna be the first place I come back to when things don't work
        return 'a'


def doShift():
    cyphtxt = 'bx re yh zy bf lm kt ut yg se tb sx ky co jh km aq ve tx vx cy ji ut vt kn vc gx aw ij av qn lg ef fj uq bd kn sv'
    testCyph = 'ocfyeuq w avtv fvxzi jovxtekuql yirov rvy zz hbti ja cny wtusgamjfg vhr dmyx bwv at moid rck P oeak moi nqgmlve'
    newtxt = testCyph.replace(" ", "")
    print(newtxt)

    # for every set of 3
    firstLet = 't'
    secondLet = 'h'
    thirdLet = 'e'
    for i in range(len(newtxt) - 2):
        print(i)
        move1 = findMove(newtxt[i], firstLet)
        char1 = setChar(move1)
        move2 = findMove(newtxt[i+1], secondLet)
        char2 = setChar(move2)
        move3 = findMove(newtxt[i+2], thirdLet)
        char3 = setChar(move3)

        partialCrib = char1 + char2 + char3
        print(partialCrib)


if __name__ == '__main__':
    doShift()
