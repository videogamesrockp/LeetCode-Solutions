class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> nums_map = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i ++) {
            nums_map.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i ++) {
            if (nums_map.containsKey(target - nums[i])) {
                if (nums_map.get(target - nums[i]) != i) {
                    return new int[]{nums_map.get(target - nums[i]), i};
                }
            }
        }
        return new int[2];
    }
}