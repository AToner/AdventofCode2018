from collections import defaultdict


def coords_at_time(board_definition, time=0):
    coords = []

    largest_x = 0
    largest_y = 0
    smallest_x = 0
    smallest_y = 0

    for line in board_definition:
        first_open = line.find('<')
        first_close = line.find('>', first_open)

        second_open = line.find('<', first_close)
        second_close = line.find('>', second_open)

        position = list(map(int, line[first_open + 1:first_close].split(',')))
        velocity = list(map(int, line[second_open + 1:second_close].split(',')))

        x = position[0] + (velocity[0] * time)
        y = position[1] + (velocity[1] * time)

        largest_x = max(largest_x, x)
        largest_y = max(largest_y, y)

        smallest_x = min(smallest_x, x)
        smallest_y = min(smallest_y, y)

        coords.append((x, y))

    size = (smallest_x, largest_x + 1, smallest_y, largest_y + 1)

    board = defaultdict(int)

    for coord in coords:
        x, y = coord
        board[(x, y)] = 1

    return size, board


def part_one_and_two(input_data):
    size, board = coords_at_time(input_data, 0)
    smallest_x, largest_x, smallest_y, largest_y = size
    y_range = largest_y - smallest_y
    last_y_range = y_range

    time = 1
    while True:
        size, board = coords_at_time(input_data, time)
        smallest_x, largest_x, smallest_y, largest_y = size
        y_range = largest_y - smallest_y

        if last_y_range < y_range:
            size, board = coords_at_time(input_data, time - 1)
            break

        time += 1

        last_y_range = y_range

    for y in range(smallest_y, largest_y):
        for x in range(smallest_x, largest_x):
            if board[(x, y)] == 1:
                print('.', end='')
            else:
                print(' ', end='')
        print()

    print(time - 1)


test_input = ['position=< 9,  1> velocity=< 0,  2>',
              'position=< 7,  0> velocity=<-1,  0>',
              'position=< 3, -2> velocity=<-1,  1>',
              'position=< 6, 10> velocity=<-2, -1>',
              'position=< 2, -4> velocity=< 2,  2>',
              'position=<-6, 10> velocity=< 2, -2>',
              'position=< 1,  8> velocity=< 1, -1>',
              'position=< 1,  7> velocity=< 1,  0>',
              'position=<-3, 11> velocity=< 1, -2>',
              'position=< 7,  6> velocity=<-1, -1>',
              'position=<-2,  3> velocity=< 1,  0>',
              'position=<-4,  3> velocity=< 2,  0>',
              'position=<10, -3> velocity=<-1,  1>',
              'position=< 5, 11> velocity=< 1, -2>',
              'position=< 4,  7> velocity=< 0, -1>',
              'position=< 8, -2> velocity=< 0,  1>',
              'position=<15,  0> velocity=<-2,  0>',
              'position=< 1,  6> velocity=< 1,  0>',
              'position=< 8,  9> velocity=< 0, -1>',
              'position=< 3,  3> velocity=<-1,  1>',
              'position=< 0,  5> velocity=< 0, -1>',
              'position=<-2,  2> velocity=< 2,  0>',
              'position=< 5, -2> velocity=< 1,  2>',
              'position=< 1,  4> velocity=< 2,  1>',
              'position=<-2,  7> velocity=< 2, -2>',
              'position=< 3,  6> velocity=<-1, -1>',
              'position=< 5,  0> velocity=< 1,  0>',
              'position=<-6,  0> velocity=< 2,  0>',
              'position=< 5,  9> velocity=< 1, -2>',
              'position=<14,  7> velocity=<-2,  0>',
              'position=<-3,  6> velocity=< 2, -1>']
part_one_and_two(test_input)

with open("Day10.txt") as file:
    file_text = file.readlines()

part_one_and_two(file_text)
