import java.util.*;

class Main {
    private final TreeMap<Integer, Integer> map;

    public Main() {
        map = new TreeMap<>();
    }

    public boolean book(int start, int end) {
        // Common case:
        // set: 1,2  2,4  3,4
        // Check the first element of current
        // against the second element of the lower element
        // if intercepts, add false,
        // otherwise, add true to res and [] to set
        Integer lower = map.floorKey(start);
        if (lower != null && map.get(lower) > start) {
            return false;
        }

        // set: 14,20  15,20  8,15
        // Also get higher, then check if
        // end is greater than the first el of higher
        // if yes, return false
        // else return true
        Integer higher = map.ceilingKey(start);
        if (higher != null && end > higher) {
            return false;
        }

        map.merge(start, end, Integer::sum);
        return true;
    }

    public static void main(String[] args) {
        Main main = new Main();
        int[][] nums = {{1,2}, {14,20}, {5,7}, {8,15}, {6,7}};
        List<Boolean> res = new ArrayList<>();
        for (int[] num : nums) {
            boolean isValid = main.book(num[0], num[1]);
            res.add(isValid);
        }
        System.out.println(res);
    }
}