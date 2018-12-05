import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collectors;

/*
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
*/
public class Day2 {
    private ArrayList<String> inputStrings;

    public Day2(String fileName) {
        inputStrings = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            for (String line; (line = br.readLine()) != null; ) {
                inputStrings.add(line);
            }
        } catch (IOException e) {
            System.out.println(e.toString());
        }
    }

    public Day2(ArrayList<String> input) {
        inputStrings = input;
    }

    private int[] twoThreeCount(String input) {
        int[] result = new int[2];

        List<Character> chars = input.chars()
                .mapToObj(c -> {
                    return (char) c;
                })
                .collect(Collectors.toList());

        HashSet<Character> mySet = new HashSet<>(chars);

        int twoCount, threeCount;
        twoCount = threeCount = 0;

        for (char thisCharacter : mySet) {
            var count = input.chars().filter(ch -> {
                return ch == thisCharacter;
            }).count();
            if (count == 2) twoCount++;
            if (count == 3) threeCount++;
        }

        result[0] = twoCount;
        result[1] = threeCount;
        return result;
    }

    private String RemoveSingleCommonCharacter(String ID1, String ID2) {
        ArrayList<Integer> differencePositions = new ArrayList<>();

        for (int i = 0; i < ID1.length(); i++) {
            if (ID1.charAt(i) != ID2.charAt(i)) {
                differencePositions.add(i);
            }
        }

        if (differencePositions.size() == 1) {
            int position = differencePositions.get(0);
            return ID1.substring(0, position) + ID1.substring(position + 1);
        }

        return ID1;
    }


    public int PartOne() {
        int twoCounter = 0;
        int threeCounter = 0;
        for (String line : inputStrings) {
            int[] counts = twoThreeCount(line);

            if (counts[0] > 0) twoCounter++;
            if (counts[1] > 0) threeCounter++;
        }

        return twoCounter * threeCounter;
    }

    public String PartTwo() {
        for (String id1 : inputStrings) {
            for (String id2 : inputStrings) {
                if (!id1.equals(id2)) {
                    String common = RemoveSingleCommonCharacter(id1, id2);
                    if (common.length() == id1.length() - 1) {
                        return common;
                    }
                }
            }
        }
        return null;
    }

}
