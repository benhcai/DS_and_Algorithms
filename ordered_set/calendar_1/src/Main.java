import java.util.Arrays;
import java.util.List;
import java.util.TreeSet;

public class Main {
    List<Boolean> calendar(int[][] nums) {
        return Arrays.asList(false);
    }

    public static void main(String[] args) {
        int[][] nums1 = {{1}};
        TreeSet<Integer> set = new TreeSet<>();
        set.addAll(Arrays.asList(1,2,3,4,5));
        System.out.println(set.tailSet(2, false));
    }
}
