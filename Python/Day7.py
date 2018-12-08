"""
--- Day 7: The Sum of Its Parts ---
You find yourself standing on a snow-covered coastline; apparently, you landed a little off course. The region is too
hilly to see the North Pole from here, but you do spot some Elves that seem to be trying to unpack something that washed
ashore. It's quite cold out, so you decide to risk creating a paradox by asking them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak; you assume it's
Ancient Nordic Elvish. Could the device on your wrist also be a translator? "Those clothes don't look very warm; take
this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher priorities at the moment. You see, believe it or
not, this box contains something that will solve all of Santa's transportation problems - at least, that's what it looks like from the pictures in the instructions." It doesn't seem like they can read whatever language it's in, but you can: "Sleigh kit. Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!" They start excitedly pulling more
parts out of the box.

The instructions specify a series of steps and requirements about which steps must be finished before others can begin
(your puzzle input). Each step is designated by a single letter. For example, suppose you have the following
instructions:

Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
Visually, these requirements look like this:


  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----
Your first goal is to determine the order in which the steps should be completed. If more than one step is ready, choose
 the step which is first alphabetically. In this example, the steps would be completed as follows:

Only C is available, and so it is done first.
Next, both A and F are available. A is first alphabetically, so it is done next.
Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of
the three.
After that, only D and F are available. E is not available because only some of its prerequisites are complete.
Therefore, D is completed next.
F is the only choice, so it is done next.
Finally, E is completed.
So, in this example, the correct order is CABDFE.

In what order should the steps in your instructions be completed?

Your puzzle answer was PFKQWJSVUXEMNIHGTYDOZACRLB.

--- Part Two ---
As you're about to begin construction, four of the Elves offer to help. "The sun will set soon; it'll go faster if we
work together." Now, you need to account for multiple people working on steps simultaneously. If multiple steps are
available, workers should still begin them in alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and so on. So, step A takes
60+1=61 seconds, while step Z takes 60+26=86 seconds. No time is required between steps.

To simplify things for the example, however, suppose you only have help from one Elf (a total of two workers) and that
each step takes 60 fewer seconds (so that step A takes 1 second and step Z takes 26 seconds). Then, using the same
instructions as above, this is how each second would be spent:

Second   Worker 1   Worker 2   Done
   0        C          .
   1        C          .
   2        C          .
   3        A          F       C
   4        B          F       CA
   5        B          F       CA
   6        D          F       CAB
   7        D          F       CAB
   8        D          F       CAB
   9        D          .       CABF
  10        E          .       CABFD
  11        E          .       CABFD
  12        E          .       CABFD
  13        E          .       CABFD
  14        E          .       CABFD
  15        .          .       CABFDE
Each row represents one second of time. The Second column identifies how many seconds have passed as of the beginning of that second. Each worker column shows the step that worker is currently doing (or . if they are idle). The Done column shows completed steps.

Note that the order of the steps has changed; this is because steps now take time to finish and multiple workers can begin multiple steps simultaneously.

In this example, it would take 15 seconds for two workers to complete these steps.

With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps?

Your puzzle answer was 864.
"""


def build_steps(puzzle_input):
    steps = set()
    pre_reqs = {}

    for line in puzzle_input:
        step_position_1 = line.find(" must") - 1
        step_position_2 = line.find(" can ") - 1
        step_1 = line[step_position_1:step_position_1 + 1]
        step_2 = line[step_position_2:step_position_2 + 1]

        steps.add(step_1)
        steps.add(step_2)

        if step_2 in pre_reqs:
            pre_reqs[step_2].append(step_1)
        else:
            pre_reqs[step_2] = [step_1]

    return steps, pre_reqs


def part_one(puzzle_input):
    steps, pre_reqs = build_steps(puzzle_input)
    result = []

    available_steps = set(steps - pre_reqs.keys())

    while len(available_steps) > 0:
        available_steps = sorted(available_steps)
        this_step = available_steps[0]
        available_steps.remove(this_step)
        result.append(this_step)

        for step, pre_req in pre_reqs.items():
            if this_step in pre_req:
                pre_req.remove(this_step)
                if len(pre_req) == 0:
                    available_steps.append(step)

    return ''.join(result)


def part_two(puzzle_input, worker_count, base_time):
    steps, pre_reqs = build_steps(puzzle_input)

    steps_to_finish = steps.copy()

    worker_next_available = [0 for _ in range(worker_count)]
    time = 0

    in_progress_steps = {}
    available_steps = set(steps - pre_reqs.keys())

    # We're checking off all the tasks in the input.
    while len(steps_to_finish) > 0:
        # Find a worker that is free
        for current_worker in range(worker_count):
            if worker_next_available[current_worker] <= time:
                # Is there work for this available worker?
                if len(available_steps) > 0:
                    # Find the worker a task.  Work out when it'll be finish
                    available_steps = sorted(available_steps)
                    this_step = available_steps[0]
                    available_steps.remove(this_step)
                    step_time = (ord(this_step) - ord('A') + 1 + base_time)
                    step_finish = time + step_time
                    worker_next_available[current_worker] = step_finish

                    # Add this task to the list of tasks to check on over time.
                    in_progress_steps[this_step] = step_finish

        time += 1

        # Check to see if any running task has finished
        for this_step, end_time in in_progress_steps.items():
            if time >= end_time:
                # So we're done with this step... remove it from the check list
                if this_step in steps_to_finish:
                    steps_to_finish.remove(this_step)

                # Check the prereqs to see if this frees up another task
                for step, pre_req in pre_reqs.items():
                    if this_step in pre_req:
                        pre_req.remove(this_step)
                        if len(pre_req) == 0:
                            available_steps.append(step)

    return max(worker_next_available)


with open("Day7.txt") as file:
    file_text = file.readlines()

test_data = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.'
]
print(part_one(test_data))
print(part_one(file_text))

print(part_two(test_data, 2, 0))
print(part_two(file_text, 5, 60))
