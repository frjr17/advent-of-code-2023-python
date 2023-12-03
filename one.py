def part_one(puzzle):
    result = 0

    for line in puzzle:
        ID = int(line.split(":")[0].split(" ")[1])
        subsets = line.split(":")[1].split(";")
        is_valid = True

        for subset in subsets:
            cubes = subset.split(",")

            for cube in cubes:
                cube = cube.strip()
                quantity, color = cube.split(" ")
                quantity = int(quantity)

                if color == "red" and quantity > 12:
                    is_valid = False
                    break

                if color == "green" and quantity > 13:
                    is_valid = False
                    break

                if color == "blue" and quantity > 14:
                    is_valid = False
                    break

        if is_valid:
            result += ID

    return result
