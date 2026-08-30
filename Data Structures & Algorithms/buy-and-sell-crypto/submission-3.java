class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxProfit_ = 0; 
        while (right < prices.length) {
            int leftPrice = prices[left];
            int rightPrice = prices[right];
            if (leftPrice <= rightPrice) {
                maxProfit_ = Math.max(maxProfit_, rightPrice - leftPrice);   
            } else {
                left = right;
            }
            right++;
        }
        return maxProfit_;
    }
}
