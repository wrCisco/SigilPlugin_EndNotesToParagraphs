#!/usr/bin/env python

lowercase_letters = [chr(x) for x in range(97, 123)]
uppercase_letters = [chr(x) for x in range(65, 91)]


def italianize(case):
    if case == 'lower':
        italian_letters = lowercase_letters.copy()
        for letter in ('k', 'j', 'w', 'x', 'y'):
            italian_letters.remove(letter)
    else:
        italian_letters = uppercase_letters.copy()
        for letter in ('K', 'J', 'W', 'X', 'Y'):
            italian_letters.remove(letter)
    return italian_letters   


def intToString(counter, whichLetters):
    noteSign = ''
    while counter > 0:
        if counter % len(whichLetters):
            number = counter % len(whichLetters)
            counter -= number
            noteSign = whichLetters[number-1]+noteSign
        else:
            counter //= len(whichLetters)
    return noteSign


def intToRoman(counter, case):
    noteSign = ''
    intTuple = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    romanTuple = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    while counter > 0:
        for x in range(len(intTuple)):
            if counter >= intTuple[x]:
                if case == 'lower':
                    noteSign += romanTuple[x].lower()
                else:
                    noteSign += romanTuple[x]
                counter -= intTuple[x]
                break
    return noteSign

    
def addZeroes(counter, filler):
    return '{:0>{filler}}'.format(counter, filler=filler)


if __name__ == '__main__':
    for x in range(5):
        num = int(input("Write a number: "))
        print(intToRoman(num, 'lower'))
        print(intToString(num, italianize('upper')))
        print(intToString(num, lowercase_letters))
