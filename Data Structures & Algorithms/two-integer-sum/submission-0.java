class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.get(diff) != null) {
                int[] output = {map.get(diff), i};
                return output;
            } else {
                map.put(nums[i], i);
            }
        }
        return null;
    }
}
