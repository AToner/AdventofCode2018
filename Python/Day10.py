"""
--- Day 10: The Stars Align ---
It's no use; your navigation system simply isn't capable of providing walking directions in the arctic circle, and
certainly not in 1018.

The Elves suggest an alternative. In times like these, North Pole rescue operations will arrange points of light in the
sky to guide missing Elves back to base. Unfortunately, the message is easy to miss: the points move slowly enough that
it takes hours to align them, but have so much momentum that they only stay aligned for a second. If you blink at the
wrong time, it might be hours before another message appears.

You can see these points of light floating in the distance, and record their position in the sky and their velocity, the
relative change in position per second (your puzzle input). The coordinates are all given from your perspective; given
enough time, those positions and velocities will move the points into a cohesive message!

Rather than wait, you decide to fast-forward the process and calculate what the points will eventually spell.

For example, suppose you note the following points:

position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
Each line represents one point. Positions are given as <X, Y> pairs: X represents how far left (negative) or right
(positive) the point appears, while Y represents how far up (negative) or down (positive) the point appears.

At 0 seconds, each point has the position given. Each second, each point's velocity is added to its position. So, a
point with velocity <1, -2> is moving to the right, but is moving upward twice as quickly. If this point's initial
position were <3, 9>, after 3 seconds, its position would become <6, 3>.

Over time, the points listed above would move like this:

Initially:
........#.............
................#.....
.........#.#..#.......
......................
#..........#.#.......#
...............#......
....#.................
..#.#....#............
.......#..............
......#...............
...#...#.#...#........
....#..#..#.........#.
.......#..............
...........#..#.......
#...........#.........
...#.......#..........

After 1 second:
......................
......................
..........#....#......
........#.....#.......
..#.........#......#..
......................
......#...............
....##.........#......
......#.#.............
.....##.##..#.........
........#.#...........
........#...#.....#...
..#...........#.......
....#.....#.#.........
......................
......................

After 2 seconds:
......................
......................
......................
..............#.......
....#..#...####..#....
......................
........#....#........
......#.#.............
.......#...#..........
.......#..#..#.#......
....#....#.#..........
.....#...#...##.#.....
........#.............
......................
......................
......................

After 3 seconds:
......................
......................
......................
......................
......#...#..###......
......#...#...#.......
......#...#...#.......
......#####...#.......
......#...#...#.......
......#...#...#.......
......#...#...#.......
......#...#..###......
......................
......................
......................
......................

After 4 seconds:
......................
......................
......................
............#.........
........##...#.#......
......#.....#..#......
.....#..##.##.#.......
.......##.#....#......
...........#....#.....
..............#.......
....#......#...#......
.....#.....##.........
...............#......
...............#......
......................
......................
After 3 seconds, the message appeared briefly: HI. Of course, your message will be much longer and will take many more
seconds to appear.

What message will eventually appear in the sky?

Your puzzle answer was EKALLKLB.

--- Part Two ---
Good thing you didn't have to wait, because that would have taken a long time - much longer than the 3 seconds in the
example above.

Impressed by your sub-hour communication capabilities, the Elves are curious: exactly how many seconds would they have
needed to wait for that message to appear?

Your puzzle answer was 10227.
"""

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
