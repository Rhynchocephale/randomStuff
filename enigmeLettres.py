#!/usr/bin/env python2.7
from num2words import num2words
import re

vowels = "aeiouy"
regex = re.compile('[^a-zA-Z]')

def lettersOnly(s):
    return regex.sub('', s)

def countVowelsAndConsonnants(s):
    s = lettersOnly(s).lower()
    num_vowels=0
    num_consonnants=0
    for char in s:
        if char in vowels:
           num_vowels += 1
        else:
           num_consonnants += 1
    return [num_vowels, num_consonnants]

base_string = "Cette phrase est composee de X consonnes et de Z voyelles"

for v in range(17,201):
    if not v%100:
        print(v)
    for c in range(24,201):

        count = countVowelsAndConsonnants(base_string.replace("X", num2words(c, lang='fr')).replace("Z", num2words(v, lang='fr')))
        if v == count[0] and c == count[1]:
            print("----------------\nv="+str(v)+"; c="+str(c)+"\n----------------")
            exit(0)
