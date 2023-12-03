def part_one(puzzle):
    result = 0

    for line in puzzle:
        results = [0 for letter in line]
        i = 0
        for letter in line:
            try:
                results[i] = int(letter)
            except:
                pass
            i += 1
        results = [result for result in results if result != 0]

        result += int("".join([str(results[0]), str(results[-1])]))

    return result
