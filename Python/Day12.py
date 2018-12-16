def parse_input(input_lines):
    initial_state = input_lines[0].strip().replace('initial state: ', '')

    rules = {}
    for line in input_lines[2:]:
        line = line.strip()
        rule_end = line.find(' => ')
        result = line[-1]
        rules[line[:rule_end]] = result

    print(initial_state, rules)
    return initial_state, rules


def age_plants(initial_state, rules, generations):
    all_generations = [initial_state]
    offset = 0

    for gen in range(generations):

        if initial_state[0] == '#':
            initial_state = '...' + initial_state
            offset -= 3

        result = ''
        for i in range(len(initial_state) + 1):
            this_plant = initial_state[i - 2:i + 3].ljust(5, '.')

            if this_plant in rules:
                result += rules[this_plant]
            else:
                result += '.'

        initial_state = result
        all_generations.append(result)

    return all_generations, offset


def part_one(input_data, generations):
    result = 0
    initial_state, rules = parse_input(input_data)
    generations, offset = age_plants(initial_state, rules, generations)

    for i, pot in enumerate(generations[len(generations) - 1]):
        if pot == '#':
            result = result + offset + i

    return result


test_input = [
    'initial state: #..#.#..##......###...###',
    '',
    '...## => #',
    '..#.. => #',
    '.#... => #',
    '.#.#. => #',
    '.#.## => #',
    '.##.. => #',
    '.#### => #',
    '#.#.# => #',
    '#.### => #',
    '##.#. => #',
    '##.## => #',
    '###.. => #',
    '###.# => #',
    '####. => #'
]

print(part_one(test_input, 20))

with open("Day12.txt") as file:
    file_text = file.readlines()

print(part_one(file_text, 20))
print(part_one(file_text, 50000000000))

# 1874
