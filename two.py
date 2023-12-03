def part_two(puzzle):
    result = 0
    num_dict = {"one": 1, "two": 2, "three": 3, "four": 4,
                "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for line in puzzle:
        results = [0 for letter in line]
        i = 0
        for letter in line:
            try:
                results[i] = int(letter)
            except:
                pass
            i += 1

        for key, value in num_dict.items():
            index = line.find(key)

            while index != -1:
                results[index] = value
                index = line.find(key, index+1)

        results = [result for result in results if result != 0]
        result += int("".join([str(results[0]), str(results[-1])]))

    return result
