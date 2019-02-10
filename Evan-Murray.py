#!/usr/bin/env python3
import math
import os
'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''


def main():
    # Test for the Reverse function
    print('\n\nReverse String test:\n')
    print('Normal: Hello, Reversed: {}'.format(reverse('Hello')))
    print('Normal: Python, Reversed: {}'.format(reverse('Python')))
    print('Normal: Onomatopoeia, Reversed: {}'.format(reverse('Onomatopoeia')))

    # Test for Acronym function
    print('\n\nAcronym test:\n')
    print('Phrase: Portable Network Graphics, Acronym: {}'.format(acronym('Portable Network Graphics')))
    print('Phrase: Laugh Out Loud, Acronym: {}'.format(acronym('Laugh Out Loud')))
    print('Phrase: First In Last Out, Acronym: {}'.format(acronym('First In Last Out')))

    # Test for Triangle Type function
    print('\n\nTriangle Type test:\n')
    print(whichTriangle(30,60,60))
    print(whichTriangle(42.4,50,66.3))
    print(whichTriangle(40,40,40))

    # Test for Scrabble Value
    print('\n\nScrabble Value test:\n')
    print('cabbage, value: {}'.format(scrabble('cabbage')))
    print('fluorescent, value: {}'.format(scrabble('fluorescent')))
    print('excellent, value: {}'.format(scrabble('excellent')))

    # Test for Armstrong Number function
    print('\n\nArmstrong Number test:\n')
    print('9: {}'.format(armstrong(9)))
    print('10: {}'.format(armstrong(10)))
    print('153: {}'.format(armstrong(153)))
    print('154: {}'.format(armstrong(154)))

    # Test for Prime Factorization function
    print('\n\n Prime Factorization test:\n')
    print('100\n{}'.format(primeFactors(100)))
    print('27\n{}'.format(primeFactors(27)))
    print('4365\n{}'.format(primeFactors(4365)))

    # Test for Pangram function
    print('\n\nPangram test:\n')
    print('The quick brown fox jumps over the lazy dog, Is a pangram: {}'.format(pangram('The quick brown fox jumps over the lazy dog')))
    print('This sentence is not a pangram,  Is a pangram: {}'.format(pangram('This sentence is not a pangram')))
    print('Five hexing wizard bots jump quickly,  Is a pangram: {}'.format(pangram('Five hexing wizard bots jump quickly')))

    # Test for Number Sort function
    print('\n\nNumber Sort test:\n')
    print('[2, 4, 5, 1, 3, 1] -> {}'.format(sort([2,4,5,1,3,1])))
    print('[7, 7, 2, 4, 1, 9, 5, 0] -> {}'.format(sort([7,7,2,4,1,9,5,0])))
    print('[1, 3, 6, 2, 9, 10, 0, 25] -> {}'.format(sort([1,3,6,2,9,10,0,25])))

    print('\n\nRotate Cipher test:\n')
    # Test for Rotate Cipher function
    print(rotate(13, 'abcdefghijklmnopqrstuvwxyz'))
    print(rotate(4, 'abcdefghijklmnopqrstuvwxyz'))
    print(rotate(25, 'I am happy this works!'))

    print('\n\nEven & Odds')
    evenAndOdds()


'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''


def reverse(string):
    reversed_string = ''
    index = len(string)-1
    for i in range(index, -1, -1):
        reversed_string += string[i]
    return reversed_string


'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''


def acronym(phrase):
    result = ''
    trimmed_phrase = phrase.strip()
    words = trimmed_phrase.split(' ')
    for word in words:
        result += word[0]
    return result


'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
    if sideOne == sideTwo and sideTwo == sideThree:
        return 'equilateral'
    elif sideOne == sideTwo or sideOne == sideThree or sideTwo == sideThree :
        return 'isoceles'
    else:
        return 'scalene'
'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
    letter_values = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'R':1, 'S':1, 'T':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10}
    total = 0
    for letter in word:
        total += letter_values[letter.upper()]
    return total
'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
def armstrong(number):
    result = 0
    string = str(number)
    power = len(string)
    for x in string:
        result += int(x) ** power
    if result == number:
        return True
    else:
        return False
'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def primeFactors(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2
    for x in range(3,int(math.sqrt(number))+1,2):
        while number % x == 0:
            factors.append(x)
            number /= x
    if number > 2:
        factors.append(number)

    return factors

'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
def pangram(sentence):
    alphabet = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T', 'D', 'G', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z'}
    test_set = set()
    for letter in sentence:
        test_set.add(letter.upper())
    if len(alphabet & test_set) == 26:
        return True
    else: return False
'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
def sort(numbers):
    size = len(numbers)
    sorted_list = []
    while len(sorted_list) != size:
        smallest = numbers[0]
        for x in numbers:
            if x < smallest:
                smallest = x
        sorted_list.append(smallest)
        numbers.remove(smallest)
    return sorted_list

'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
def rotate(key, string):
    if key == 0 or key == 26:
        return string
    if key < 0 or key > 26 or not str(key).isdigit():
        return "Use a key between 0-26"
    alphabet = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13,
     'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    result = ''
    for letter in string:
        if letter.isalpha():
            value = alphabet[letter.upper()]
            value += key
            if value > 26:
                value -= 26
            for k, v in alphabet.items():
                if value == v:
                    result = result + k.lower()
        else:
            result = result + letter
    return result

'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
def evenAndOdds():
    for i in range(0, 10, 1):
        num = ''
        while not num.isdigit():
            num = input('{}: Enter a number...'.format(i))
        if int(num) % 2 == 0:
            os.system('echo {} >> even.txt'.format(num))
        else:
            os.system('echo {} >> odd.txt'.format(num))
if(__name__ == '__main__'):
    main()
