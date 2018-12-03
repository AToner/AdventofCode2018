"""
--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully
wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting
them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist
of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from
the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and
ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas.
For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not
overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric
are within two or more claims?

Your puzzle answer was 116489.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any
other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?
"""


def create_cloth(input):
    test_data = []
    largest_height = 0
    largest_width = 0
    for claim in input:
        position_start = claim.find('@ ') + 2
        position_end = claim.find(': ')
        size_start = position_end + 2

        claim_number = int(claim[1:position_start - 2])
        position = list(map(int, claim[position_start:position_end].split(',')))
        size = list(map(int, claim[size_start:].split('x')))
        test_data.append([claim_number, position, size])

        largest_width = max(position[0] + size[0], largest_width)
        largest_height = max(position[1] + size[1], largest_width)

    cloth = [[[] for _ in range(largest_width + 1)] for _ in range(largest_height + 1)]

    for claim in test_data:
        number = claim[0]
        position = claim[1]
        size = claim[2]
        for width in range(position[0], position[0] + size[0]):
            for height in range(position[1], position[1] + size[1]):
                cloth[height][width].append(number)

    return cloth


def part_one(input):
    cloth = create_cloth(input)
    overlap = 0
    for row in cloth:
        for cell in row:
            if len(cell) > 1:
                overlap += 1
    return overlap


test_input = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
print(part_one(test_input))

with open("Day3.txt") as file:
    file_text = file.readlines()

print(part_one(file_text))
