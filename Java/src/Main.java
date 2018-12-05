import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        Day1 day1 = new Day1("Day1.txt");

        System.out.println("Day 1");
        System.out.println("Part One = " + day1.PartOne());
        System.out.println("Part Two = " + day1.PartTwo());

        Day2 day2_test = new Day2(new ArrayList<>(Arrays.asList("abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz")));
        System.out.println("Day 2 Test");
        System.out.println("Part One = " + day2_test.PartOne());
        System.out.println("Part Two = " + day2_test.PartTwo());

        Day2 day2 = new Day2("Day2.txt");
        System.out.println("Day 2");
        System.out.println("Part One = " + day2.PartOne());
        System.out.println("Part Two = " + day2.PartTwo());

    }
}
