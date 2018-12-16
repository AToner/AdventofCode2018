"""
--- Day 14: Chocolate Charts ---
You finally have a chance to look at all of the produce moving around. Chocolate, cinnamon, mint, chili peppers, nutmeg,
vanilla... the Elves must be growing these plants to make hot chocolate! As you realize this, you hear a conversation in
the distance. When you go to investigate, you discover two Elves in what appears to be a makeshift underground
kitchen/laboratory.

The Elves are trying to come up with the ultimate hot chocolate recipe; they're even maintaining a scoreboard which
tracks the quality score (0-9) of each recipe.

Only two recipes are on the board: the first recipe got a score of 3, the second, 7. Each of the two Elves has a current
recipe: the first Elf starts with the first recipe, and the second Elf starts with the second recipe.

To create new recipes, the two Elves combine their current recipes. This creates new recipes from the digits of the sum
of the current recipes' scores. With the current recipes' scores of 3 and 7, their sum is 10, and so two new recipes
would be created: the first with score 1 and the second with score 0. If the current recipes' scores were 2 and 3, the
sum, 5, would only create one recipe (with a score of 5) with its single digit.

The new recipes are added to the end of the scoreboard in the order they are created. So, after the first round, the
scoreboard is 3, 7, 1, 0.

After all new recipes are added to the scoreboard, each Elf picks a new current recipe. To do this, the Elf steps
forward through the scoreboard a number of recipes equal to 1 plus the score of their current recipe. So, after the
first round, the first Elf moves forward 1 + 3 = 4 times, while the second Elf moves forward 1 + 7 = 8 times. If they
run out of recipes, they loop back around to the beginning. After the first round, both Elves happen to loop around
until they land on the same recipe that they had in the beginning; in general, they will move to different recipes.

Drawing the first Elf as parentheses and the second Elf as square brackets, they continue this process:

(3)[7]
(3)[7] 1  0
 3  7  1 [0](1) 0
 3  7  1  0 [1] 0 (1)
(3) 7  1  0  1  0 [1] 2
 3  7  1  0 (1) 0  1  2 [4]
 3  7  1 [0] 1  0 (1) 2  4  5
 3  7  1  0 [1] 0  1  2 (4) 5  1
 3 (7) 1  0  1  0 [1] 2  4  5  1  5
 3  7  1  0  1  0  1  2 [4](5) 1  5  8
 3 (7) 1  0  1  0  1  2  4  5  1  5  8 [9]
 3  7  1  0  1  0  1 [2] 4 (5) 1  5  8  9  1  6
 3  7  1  0  1  0  1  2  4  5 [1] 5  8  9  1 (6) 7
 3  7  1  0 (1) 0  1  2  4  5  1  5 [8] 9  1  6  7  7
 3  7 [1] 0  1  0 (1) 2  4  5  1  5  8  9  1  6  7  7  9
 3  7  1  0 [1] 0  1  2 (4) 5  1  5  8  9  1  6  7  7  9  2
The Elves think their skill will improve after making a few recipes (your puzzle input). However, that could take ages;
you can speed this up considerably by identifying the scores of the ten recipes after that. For example:

If the Elves think their skill will improve after making 9 recipes, the scores of the ten recipes after the first nine
on the scoreboard would be 5158916779 (highlighted in the last line of the diagram).
After 5 recipes, the scores of the next ten would be 0124515891.
After 18 recipes, the scores of the next ten would be 9251071085.
After 2018 recipes, the scores of the next ten would be 5941429882.
What are the scores of the ten recipes immediately after the number of recipes in your puzzle input?

Your puzzle answer was 7116398711.

--- Part Two ---
As it turns out, you got the Elves' plan backwards. They actually want to know how many recipes appear on the scoreboard
to the left of the first recipes whose scores are the digits from your puzzle input.

51589 first appears after 9 recipes.
01245 first appears after 5 recipes.
92510 first appears after 18 recipes.
59414 first appears after 2018 recipes.
How many recipes appear on the scoreboard to the left of the score sequence in your puzzle input?

Your puzzle answer was 20316365.
"""


class Recipe:
    def __init__(self, score=None):
        self.score = score
        self.next_recipe = None

    def __str__(self):
        return str(self.score)

    def forward(self, n):
        result = self
        for _ in range(n):
            result = result.next_recipe
        return result


class RecipeTracker:
    first_recipe = None
    last_recipe = None

    def __init__(self):
        self.recipe_count = 0

    def __str__(self):
        result = ''
        head = self.first_recipe
        for _ in range(self.recipe_count):
            result += str(head.score) + ', '
            head = head.next_recipe

        return result

    def store_recipe(self, recipe_score):
        recipe = Recipe(recipe_score)

        if self.recipe_count == 0:
            recipe.next_recipe = recipe
            self.first_recipe = recipe
            self.last_recipe = recipe
        else:
            self.last_recipe.next_recipe = recipe
            recipe.next_recipe = self.first_recipe
            self.last_recipe = recipe

        self.recipe_count += 1
        return recipe


def create_recipes(input_number):
    result = []

    for c in str(input_number):
        result.append(int(c))

    return result


def part_one(seed_recipe, after_n_recipes):
    tracker = RecipeTracker()

    starters = create_recipes(seed_recipe)
    elf_1 = tracker.store_recipe(starters[0])
    elf_2 = tracker.store_recipe(starters[1])

    for r in starters[2:]:
        tracker.store_recipe(r)

    result = []
    while tracker.recipe_count < 10 + after_n_recipes:
        new_ones = create_recipes(elf_1.score + elf_2.score)
        for recipe in new_ones:
            if tracker.recipe_count >= after_n_recipes:
                result.append(recipe)
            tracker.store_recipe(recipe)

        elf_1 = elf_1.forward(elf_1.score + 1)
        elf_2 = elf_2.forward(elf_2.score + 1)

    return ''.join(str(score) for score in result[:10])


def part_two(seed_recipe, target):
    tracker = RecipeTracker()

    starters = create_recipes(seed_recipe)
    elf_1 = tracker.store_recipe(starters[0])
    elf_2 = tracker.store_recipe(starters[1])

    for r in starters[2:]:
        tracker.store_recipe(r)

    count = 0
    result = []
    target_len = len(str(target))
    while True:
        new_ones = create_recipes(elf_1.score + elf_2.score)
        for recipe in new_ones:
            count += 1
            tracker.store_recipe(recipe)
            result.append(recipe)
            result = result[-target_len:]
            final_recipes = ''.join(str(score) for score in result)
            if final_recipes == str(target):
                return tracker.recipe_count - target_len

        elf_1 = elf_1.forward(elf_1.score + 1)
        elf_2 = elf_2.forward(elf_2.score + 1)


print(part_one(37, 9))  # 5158916779
print(part_one(37, 5))  # 0124515891
print(part_one(37, 18))  # 9251071085
print(part_one(37, 2018))  # 5941429882
print(part_one(37, 320851))  # 7116398711

print(part_two(37, '51589'))  # 9
print(part_two(37, '01245'))  # 5
print(part_two(37, '92510'))  # 18
print(part_two(37, '59414'))  # 2018
print(part_two(37, '320851'))  # 20316365
