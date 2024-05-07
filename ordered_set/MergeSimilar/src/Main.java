import java.util.TreeMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public List<List<Integer>> mergeSimilar(int[][] items1, int[][] items2) {
        Map<Integer, Integer> map = new TreeMap<>();

        for (int[] nums : items1) {
            map.merge(nums[0], nums[1], Integer::sum); // merge inserts key while maintaining ordering
        }

        for (int[] nums : items2) {
            map.merge(nums[0], nums[1], Integer::sum); // merge maintains orde
        }

        List<List<Integer>> res = new ArrayList<>();

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            res.add(Arrays.asList(entry.getKey(), entry.getValue()));
        }

        return res;
    }

    public static void main(String[] args) {
        Main main = new Main();
        int[][] items1 = {{1,2}, {4,2}, {6,1}};
        int[][] items2 = {{2,5}, {3,3}, {5, 4}};
        List<List<Integer>> res = main.mergeSimilar(items1, items2);
        System.out.println(res);
    }
}