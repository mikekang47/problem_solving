import java.util.*;

public class Solution {
  public int search(int[] nums, int target) {
        TreeMap<Integer, Integer> sortedMap = new TreeMap<>();
         
        for (int i = 0; i < nums.length; i++) {
            sortedMap.put(nums[i], i);
        }
        if (sortedMap.containsKey(target)) {
            return sortedMap.get(target);
        }
        return -1;
    }
}
