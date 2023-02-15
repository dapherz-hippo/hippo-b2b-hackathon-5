from helpers.fileReader import read_input_as_string
import os
path = os.path.join(os.path.abspath(os.getcwd()), 'day3' , 'day3.txt')
input = read_input_as_string(path)
#print(input)



count = 1


visitedLocations=[[0,0]]

santaCurrentLocation=[0,0]
robotCurrentLocation=[0,0]

santa = True

for char in input:
    if char == '^':
        if santa:
            santaCurrentLocation[1]+=1
        else:
            robotCurrentLocation[1]+=1
    if char == '<':
        if santa:
            santaCurrentLocation[0]-=1
        else:
            robotCurrentLocation[0]-=1
    if char == 'v':
        if santa:
            santaCurrentLocation[1]-=1
        else:
            robotCurrentLocation[1]-=1
    if char == '>':
        if santa:
            santaCurrentLocation[0]+=1
        else:
            robotCurrentLocation[0]+=1
    santa = not santa
    if santa:
        if santaCurrentLocation in visitedLocations:
            continue
    else:
        if robotCurrentLocation in visitedLocations:
            continue
    if santa:
        visitedLocations.append([santaCurrentLocation[0], santaCurrentLocation[1]])
    else:
        visitedLocations.append([robotCurrentLocation[0], robotCurrentLocation[1]])
    count+=1
print(count)
