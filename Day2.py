
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
