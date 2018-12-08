"""
--- Day 6: Chronal Coordinates ---
The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify
new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It
recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from
the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y
locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of
coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each
location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend
forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations,
and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the
largest area is 17.

What is the size of the largest area that isn't infinite?

Your puzzle answer was 4016.

--- Part Two ---
On the other hand, if the coordinates are safe, maybe the best you can do is try to find a region near as many
coordinates as possible.

For example, suppose you want the sum of the Manhattan distance to all of the coordinates to be less than 32. For each
location, add up the distances to all of the given coordinates; if the total of those distances is less than 32, that
location is within the desired region. Using the same coordinates as above, the resulting region looks like this:

..........
.A........
..........
...###..C.
..#D###...
..###E#...
.B.###....
..........
..........
........F.
In particular, consider the highlighted location 4,3 located at the top middle of the region. Its calculation is as
follows, where abs() is the absolute value function:

Distance to coordinate A: abs(4-1) + abs(3-1) =  5
Distance to coordinate B: abs(4-1) + abs(3-6) =  6
Distance to coordinate C: abs(4-8) + abs(3-3) =  4
Distance to coordinate D: abs(4-3) + abs(3-4) =  2
Distance to coordinate E: abs(4-5) + abs(3-5) =  3
Distance to coordinate F: abs(4-8) + abs(3-9) = 10
Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30
Because the total distance to all coordinates (30) is less than 32, the location is within the region.

This region, which also includes coordinates D and E, has a total size of 16.

Your actual region will need to be much larger than this example, though, instead including all locations with a total
distance of less than 10000.

What is the size of the region containing all locations which have a total distance to all given coordinates of less
than 10000?

Your puzzle answer was 46306.
"""


def parse_targets(puzzle_input):
    targets = {}
    max_x = max_y = 0
    target = 1

    # Parse out all the targets
    for entry in puzzle_input:
        coords = entry.split(',')
        x, y = int(coords[0]), int(coords[1])

        max_x = max(max_x, x)
        max_y = max(max_y, y)

        targets[target] = (x, y)
        target += 1

    return targets, max_x, max_y


def part_one(puzzle_input):
    targets, max_x, max_y = parse_targets(puzzle_input)

    # Create the board
    board = [[(0, max_y + max_x) for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Put the targets on the board with the distance to the nearest target (which is 0!)
    for target, location in targets.items():
        board[location[1]][location[0]] = (target, 0)

    # Loop through the board calculating the distance to each target
    # Use the shortest distance.  If there's a duplicate it's target 0.
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            for target, location in targets.items():
                current = board[y][x]
                current_distance = current[1]
                new_distance = abs(abs(x - location[0]) + abs(y - location[1]))

                if new_distance == current_distance and current_distance > 0:
                    board[y][x] = (0, current_distance)

                if new_distance < current_distance:
                    board[y][x] = (target, new_distance)

    # Aggregate all the distance entries.
    aggregation = []
    for row in board:
        for cell in row:
            aggregation.append(cell[0])

    # Find the infinite targets (the edges)
    infinite = set()
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if y == 0 or y == max_y or x == 0 or x == max_x:
                infinite.add(board[y][x][0])
    infinite.remove(0)

    # If the target is not in the infinite set... put them in the results.
    result = []
    for target, location in targets.items():
        if target not in infinite:
            result.append(aggregation.count(target))

    return max(result)


def part_two(puzzle_input, region_size):
    targets, max_x, max_y = parse_targets(puzzle_input)

    # Create the board
    board = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Loop through the board calculating the distance to each target
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            for target, location in targets.items():
                distance = abs(abs(x - location[0]) + abs(y - location[1]))
                board[y][x] += distance

    # Aggregate all the distance entries that are below the required region size
    aggregation = []
    for row in board:
        for cell in row:
            if cell < region_size:
                aggregation.append(cell)

    return len(aggregation)


with open("Day6.txt") as file:
    file_text = file.readlines()

print(part_one(['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']))
print(part_two(['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9'], 32))

print(part_one(file_text))
print(part_two(file_text, 10000))
