import java.util.TreeSet;
import java.util.Arrays;

class Main {
    boolean findPattern(int[] nums) {
        int k = Integer.MIN_VALUE;
        int j = 0;

        TreeSet<Integer> set = new TreeSet<>();

        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] < k) {
                System.out.println(Arrays.asList(nums[i],j,k));
                return true;
            }
            Integer n = set.lower(nums[i]);
            if (n != null) k = n;
            j = nums[i];
            set.add(nums[i]);
        }

        return false;
    }

    public static void main(String[] args) {
        int[] nums = {4,3,2,1,9,2,3};
        Main main = new Main();
        boolean res = main.findPattern(nums);
        System.out.println(res);
    }
}