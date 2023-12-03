from one import part_one
from two import part_two

with open("./puzzle.txt") as file:
    puzzle = [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    
    print("Advent of Code 2023 - Day 1\n")
    print("Part One:", part_one(puzzle))
    print("Part Two:", part_two(puzzle))