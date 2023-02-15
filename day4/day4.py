from helpers.fileReader import read_input_as_string
import hashlib
import os

path = os.path.join(os.path.abspath(os.getcwd()),'day1', 'input.txt')

input = 'iwrupvqb'

number = 0

while True:
    encodeString = hashlib.md5((input+str(number)).encode())
    print(encodeString.hexdigest()[:6])
    if (encodeString.hexdigest()[:6] == '000000'):
        break

    number += 1

print(number)