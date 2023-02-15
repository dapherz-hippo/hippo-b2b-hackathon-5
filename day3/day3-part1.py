from helpers.fileReader import read_input_as_string
import os
path = os.path.join(os.path.abspath(os.getcwd()), 'day3' , 'day3.txt')
input = read_input_as_string(path)
#print(input)


# answer = 2081

count = 1

visitedLocations=[[0,0]]
CurrentLocation=[0,0]

for char in input:
    if char == '^':
        CurrentLocation[1]+=1
    if char == '<':
        CurrentLocation[0]-=1
    if char == 'v':
        CurrentLocation[1]-=1
    if char == '>':
        CurrentLocation[0]+=1
        continue
    visitedLocations.append([CurrentLocation[0], CurrentLocation[1]])
    count+=1

print(count)
