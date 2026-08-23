class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = IntStream.concat(Arrays.stream(nums), Arrays.stream(nums))
                        .toArray();
        return ans;
    }
}