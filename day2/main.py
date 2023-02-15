from helpers.fileReader import read_input_as_lines

import os
from math import prod

def get_dimensions(input):
    return [ [ int(measurement) for measurement in line.split('x')] for line in input]

def get_n_shortest_dimensions(number, dimensions):
    sorted_dimensions = sorted(dimensions)
    return sorted_dimensions[:number]

def get_wrapping_paper_amount(dimension):
    length = dimension[0]
    width = dimension[1]
    height = dimension[2]

    sides = [ 2*length*width, 2*width*height, 2*length*height ]
    return sum(sides) + int(min(sides)/2)

def get_ribbon_amount(dimensions):
    shortest_dimensions = get_n_shortest_dimensions(2, dimensions)
    length_required = sum(shortest_dimensions)*2 + prod(dimensions)
    return length_required

def part1(input):
    areas = [ get_wrapping_paper_amount(dimensions) for dimensions in get_dimensions(input)]

    return sum(areas)

def part2(input):
    ribbon_lengths = [ get_ribbon_amount(dimensions) for dimensions in get_dimensions(input)]

    return sum(ribbon_lengths)

def main():
    path = os.path.join(os.path.abspath(os.getcwd()), 'day2', 'input.txt')
    input = read_input_as_lines(path)

    wrapping_paper_amount = part1(input)
    print(wrapping_paper_amount)

    ribbon_length = part2(input)
    print(ribbon_length)


if __name__ == "__main__":
    main()