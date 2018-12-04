"""
--- Day 2: Inventory Management System ---
You stop falling through time, catch your breath, and check the screen on the device. "Destination reached. Current Year: 1518. Current Location: North Pole Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that so many people have chimneys, maybe he could sneak in that way?" Another voice responds, "Actually, we've been working on a new kind of suit that would let him fit through tight spaces like that. But, I heard that a few days ago, they lost the prototype fabric, the design plans, everything! Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs should be similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk too far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?

Your puzzle answer was 7163.

--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)

Your puzzle answer was ighfbyijnoumxjlxevacpwqtr.
"""


def two_three_count(input_line):
    characters = list(input_line.strip())
    characters.sort()

    last_char = ''
    current_counter = 0

    two_count = 0
    three_count = 0

    for i, char in enumerate(characters):
        if char == last_char:
            current_counter += 1

        if char != last_char or i == len(characters) - 1:
            if current_counter == 2:
                two_count += 1
            elif current_counter == 3:
                three_count += 1

            current_counter = 1

        last_char = char

    return two_count, three_count


def remove_single_common_character(id_1, id_2):
    difference_positions = []
    for i, char in enumerate(id_1):
        if id_2[i] != char:
            difference_positions.append(i)

    if len(difference_positions) == 1:
        position = difference_positions[0]
        return id_1[:position] + id_1[position + 1:]

    return id_1


def part_one(input_lines):
    two_counter = 0
    three_counter = 0
    for each_line in input_lines:
        counters = two_three_count(each_line)
        if counters[0] > 0:
            two_counter += 1

        if counters[1] > 0:
            three_counter += 1

    return two_counter * three_counter


def part_two(input_lines):

    for id_1 in input_lines:
        id_1 = id_1.strip()
        for id_2 in input_lines:
            id_2 = id_2.strip()
            if id_1 != id_2:
                common = remove_single_common_character(id_1, id_2)
                if len(common) == len(id_1) - 1:
                    return common

    return ''

print(part_one(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']))  # 12

with open("Day2.txt") as file:
    file_text = file.readlines()

print(part_one(file_text))  # 7163

print(part_two(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']))
print(part_two(file_text))
