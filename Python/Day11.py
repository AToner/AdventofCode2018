def power_level(x, y, serial_number):
    power_level = x + 10
    power_level = power_level * y
    power_level += serial_number
    power_level *= (x + 10)

    hundreds = str(power_level)
    if len(hundreds) < 3:
        power_level = 0
    else:
        power_level = int(hundreds[-3])

    return power_level - 5


def part_one_and_two(serial_number, grid_size_max):
    max_dimension = 300
    largest_location = None
    largest_power = -10000
    largest_gridsize = 0

    board = [[0 for _ in range(max_dimension)] for _ in range(max_dimension)]
    for x in range(max_dimension):
        for y in range(max_dimension):
            board[y][x] = power_level(x, y, serial_number)

    for x in range(max_dimension):
        for y in range(max_dimension):

            remaining_x = max_dimension - x
            remaining_y = max_dimension - y
            remaining = min(remaining_x, remaining_y, grid_size_max)
            sum = board[y][x]
            for n in range(1, remaining):
                for i in range(n):
                    sum += board[y + i][x + n]
                    sum += board[y + n][x + i]

                sum += board[y + n][x + n]

                if sum > largest_power:
                    largest_location = (x, y)
                    largest_gridsize = n + 1
                    largest_power = sum

    return largest_location, largest_power, largest_gridsize


# print(part_one_and_two(18, 3))
# print(part_one_and_two(42, 3))
# print(part_one_and_two(3214, 3))

#print(part_one_and_two(18, 16)) # ((90, 269), 113, 16)
#print(part_one_and_two(42, 16)) # ((232, 251), 119, 12)
print(part_one_and_two(3214, 32))
