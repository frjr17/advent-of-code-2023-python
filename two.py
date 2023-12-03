def part_two(puzzle):
    result = 0

    for line in puzzle:
        ID = int(line.split(":")[0].split(" ")[1])
        subsets = line.split(":")[1].split(";")
        colors_dict = {}
        is_valid = True

        for subset in subsets:
            cubes = subset.split(",")

            for cube in cubes:
                cube = cube.strip()
                quantity, color = cube.split(" ")
                quantity = int(quantity)

                if color not in colors_dict.keys():
                    colors_dict[color] = [quantity]
                else:
                    colors_dict[color].append(quantity)

        result += (max(colors_dict["red"]) *
                   max(colors_dict["green"]) * max(colors_dict["blue"]))

    return result
