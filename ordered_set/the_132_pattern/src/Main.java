import java.util.Arrays;
import java.util.TreeSet;

public class Main {
    boolean findPattern(int[] nums) {
        TreeSet<Integer> set = new TreeSet<>();

        int k = Integer.MIN_VALUE;
        int j = -1;

        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] < k) {
                System.out.println(Arrays.asList(nums[i],j,k));
                return true;
            }

            Integer n = set.lower(nums[i]);
            if (n != null) {
                k = n;
                j = nums[i];
            }

            set.add(nums[i]);
        }

        return false;
    }

    public static void main(String[] args) {
        int[] nums1 = {1,2,3,4,5};
        int[] nums2 = {8,7,6,5,4};
        int[] nums3 = {3,6,1};
        int[] nums4 = {9,8,1,7,8,6,2};

        Main main = new Main();
        System.out.println(main.findPattern(nums1));
        System.out.println(main.findPattern(nums2));
        System.out.println(main.findPattern(nums3));
        System.out.println(main.findPattern(nums4));
    }
}
