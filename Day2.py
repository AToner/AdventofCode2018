
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


print(part_one(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']))  # 12

with open("Day2.txt") as file:
    file_text = file.readlines()

print(part_one(file_text))  # 7163
