import java.util.TreeMap;

public class Main {
    public Integer findLength(int[] nums, int limit) {
        TreeMap<Integer, Integer> map = new TreeMap<>();

        int left = 0;
        int maxLen = 0;
        for (int right = 0; right < nums.length; right++) {
            map.merge(nums[right], 1, Integer::sum);
            while (map.lastKey() - map.firstKey() > limit) {
                map.merge(nums[left], -1, Integer::sum);
                if (map.get(nums[left]) == 0) {
                    map.remove(nums[left]);
                }
                left += 1;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
    public static void main(String[] args) {
        int[] nums = {4,2,2,2,4,4,2,2};
        int limit = 0;
        Main main = new Main();
        System.out.println(main.findLength(nums, limit));
    }
}
