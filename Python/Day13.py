"""
--- Day 13: Mine Cart Madness ---
A crop of this size requires significant logistics to transport produce, soil, fertilizer, and so on. The Elves are
very busy pushing things around in carts on some kind of rudimentary system of tracks they've come up with.

Seeing as how cart-and-track systems don't appear in recorded history for another 1000 years, the Elves seem to be
making this up as they go along. They haven't even figured out how to avoid collisions yet.

You map out the tracks (your puzzle input) and see where you can help.

Tracks consist of straight paths (| and -), curves (/ and \), and intersections (+). Curves connect exactly two
perpendicular pieces of track; for example, this is a closed loop:

/----\
|    |
|    |
\----/
Intersections occur when two perpendicular paths cross. At an intersection, a cart is capable of turning left, turning
right, or continuing straight. Here are two loops connected by two intersections:

/-----\
|     |
|  /--+--\
|  |  |  |
\--+--/  |
   |     |
   \-----/
Several carts are also on the tracks. Carts always face either up (^), down (v), left (<), or right (>). (On your
initial map, the track under each cart is a straight path matching the direction the cart is facing.)

Each time a cart has the option to turn (by arriving at any intersection), it turns left the first time, goes straight
the second time, turns right the third time, and then repeats those directions starting again with left the fourth time,
straight the fifth time, and so on. This process is independent of the particular intersection at which the cart has arrived - that is, the cart has no per-intersection memory.

Carts all move at the same speed; they take turns moving a single step at a time. They do this based on their current
location: carts on the top row move first (acting from left to right), then carts on the second row move (again from
left to right), then carts on the third row, and so on. Once each cart has moved one step, the process repeats; each of
these loops is called a tick.

For example, suppose there are two carts on a straight track:

|  |  |  |  |
v  |  |  |  |
|  v  v  |  |
|  |  |  v  X
|  |  ^  ^  |
^  ^  |  |  |
|  |  |  |  |
First, the top cart moves. It is facing down (v), so it moves down one square. Second, the bottom cart moves. It is
facing up (^), so it moves up one square. Because all carts have moved, the first tick ends. Then, the process repeats,
starting with the first cart. The first cart moves down, then the second cart moves up - right into the first cart,
colliding with it! (The location of the crash is marked with an X.) This ends the second and last tick.

Here is a longer example:

/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/

/-->\
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \->--/
  \------/

/---v
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+>-/
  \------/

/---\
|   v  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+->/
  \------/

/---\
|   |  /----\
| /->--+-\  |
| | |  | |  |
\-+-/  \-+--^
  \------/

/---\
|   |  /----\
| /-+>-+-\  |
| | |  | |  ^
\-+-/  \-+--/
  \------/

/---\
|   |  /----\
| /-+->+-\  ^
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /----<
| /-+-->-\  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /---<\
| /-+--+>\  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /--<-\
| /-+--+-v  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /-<--\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/

/---\
|   |  /<---\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-<--/
  \------/

/---\
|   |  v----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \<+--/
  \------/

/---\
|   |  /----\
| /-+--v-\  |
| | |  | |  |
\-+-/  ^-+--/
  \------/

/---\
|   |  /----\
| /-+--+-\  |
| | |  X |  |
\-+-/  \-+--/
  \------/
After following their respective paths for a while, the carts eventually crash. To help prevent crashes, you'd like to
know the location of the first crash. Locations are given in X,Y coordinates, where the furthest left column is X=0 and
the furthest top row is Y=0:

           111
 0123456789012
0/---\
1|   |  /----\
2| /-+--+-\  |
3| | |  X |  |
4\-+-/  \-+--/
5  \------/
In this example, the location of the first crash is 7,3.

Your puzzle answer was 53,133.

--- Part Two ---
There isn't much you can do to prevent crashes in this ridiculous system. However, by predicting the crashes, the Elves
know where to be in advance and instantly remove the two crashing carts the moment any crash occurs.

They can proceed like this for a while, but eventually, they're going to run out of carts. It could be useful to figure
out where the last cart that hasn't crashed will end up.

For example:

/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/

/---\
|   |
| v-+-\
| | | |
\-+-/ |
  |   |
  ^---^

/---\
|   |
| /-+-\
| v | |
\-+-/ |
  ^   ^
  \---/

/---\
|   |
| /-+-\
| | | |
\-+-/ ^
  |   |
  \---/
After four very expensive crashes, a tick ends with only one cart remaining; its final location is 6,4.

What is the location of the last cart at the end of the first tick where it is the only cart left?

Your puzzle answer was 111,68.



"""


class Cart:
    def __init__(self):
        self.location = None
        self.direction = None
        self.last_turn = 0

    def __str__(self):
        return str(self.location) + ' ' + str(self.direction)

    def __lt__(self, other):
        x, y = self.location
        other_x, other_y = other.location

        if y == other_y:
            return x < other_x

        return y < other_y

    def __gt__(self, other):
        x, y = self.location
        other_x, other_y = other.location

        if x == other_x:
            return y < other_y

        return x < other_x

    def next_direction(self):
        if self.last_turn == 0 or self.last_turn == 3:
            self.last_turn = 1
        else:
            self.last_turn += 1

        if self.last_turn == 1:  # left
            if self.direction == '<':
                self.direction = 'v'
            elif self.direction == '>':
                self.direction = '^'
            elif self.direction == '^':
                self.direction = '<'
            elif self.direction == 'v':
                self.direction = '>'
        elif self.last_turn == 3:  # right
            if self.direction == '<':
                self.direction = '^'
            elif self.direction == '>':
                self.direction = 'v'
            elif self.direction == '^':
                self.direction = '>'
            elif self.direction == 'v':
                self.direction = '<'


def create_railroad(input_data):
    carts = []

    y_size = len(input_data)
    x_size = 0
    for input_line in input_data:
        x_size = max(len(input_line), x_size)

    railroad = [[' ' for _ in range(x_size)] for _ in range(y_size)]
    for y, input_line in enumerate(input_data):
        for x, c in enumerate(input_line):
            if c in ['^', 'v', '<', '>']:
                cart = Cart()
                cart.location = (x, y)
                cart.direction = c
                carts.append(cart)
                if c in ['^', 'v']:
                    railroad[y][x] = '|'
                else:
                    railroad[y][x] = '-'
            else:
                railroad[y][x] = c

    return railroad, carts


def make_turn(cart, track_piece):
    if track_piece == '/':
        if cart.direction == '<':
            cart.direction = 'v'
        elif cart.direction == '>':
            cart.direction = '^'
        elif cart.direction == '^':
            cart.direction = '>'
        elif cart.direction == 'v':
            cart.direction = '<'
    elif track_piece == '\\':
        if cart.direction == '<':
            cart.direction = '^'
        elif cart.direction == '>':
            cart.direction = 'v'
        elif cart.direction == '^':
            cart.direction = '<'
        elif cart.direction == 'v':
            cart.direction = '>'
    elif track_piece == '+':
        cart.next_direction()


def check_crashed_carts(carts):
    crashed_carts = set()
    for cart_1 in carts:
        for cart_2 in carts:
            if cart_1 is not cart_2:
                if cart_1.location == cart_2.location:
                    crashed_carts.add(cart_1)
                    crashed_carts.add(cart_2)

    return crashed_carts


def part_one(input_data):
    railroad, carts = create_railroad(input_data)

    while True:
        for cart in carts:
            location_x, location_y = cart.location
            if cart.direction == '^':
                location_y -= 1
            elif cart.direction == 'v':
                location_y += 1
            elif cart.direction == '<':
                location_x -= 1
            elif cart.direction == '>':
                location_x += 1

            cart.location = (location_x, location_y)

            make_turn(cart, railroad[location_y][location_x])

        for cart_1 in carts:
            for cart_2 in carts:
                if cart_1 is not cart_2:
                    if cart_1.location == cart_2.location:
                        return cart_1.location


def part_two(input_data):
    railroad, carts = create_railroad(input_data)

    while len(carts) > 1:
        crashed_carts = []

        for cart in sorted(carts):
            location_x, location_y = cart.location
            if cart.direction == '^':
                location_y -= 1
            elif cart.direction == 'v':
                location_y += 1
            elif cart.direction == '<':
                location_x -= 1
            elif cart.direction == '>':
                location_x += 1

            cart.location = (location_x, location_y)

            make_turn(cart, railroad[location_y][location_x])
            crashed_carts.extend(check_crashed_carts(carts))

        for cart in crashed_carts:
            if cart in carts:
                carts.remove(cart)

    return carts[0].location


with open("Day13.txt") as file:
    file_text = file.readlines()

test_data = [
    '/->-\\',
    '|   |  /----\\',
    '| /-+--+-\\  |',
    '| | |  | v  |',
    '\\-+-/  \-+--/',
    '  \\------/'
]

print(part_one(test_data))  # (7,3)
print(part_one(file_text))  # (53,133)

test_data = [
    '/>-<\\',
    '|   |',
    '| /<+-\\',
    '| | | v',
    '\\>+</ |',
    '  |   ^',
    '  \\<->/'
]

print(part_two(test_data))  # (6,4)
print(part_two(file_text))  # (111, 68)
