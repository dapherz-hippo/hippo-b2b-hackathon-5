
from helpers.fileReader import read_input_as_string
import os

path = os.path.join(os.path.abspath(os.getcwd()),'day1', 'input.txt')

input = read_input_as_string(path)

floor = 0
position = 0

for char in input:
    position += 1
    if char == '(':
        floor += 1

    if char == ')':
        floor -= 1

    if floor == -1:
        break

print(position)

