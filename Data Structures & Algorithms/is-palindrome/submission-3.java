class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            char leftChar = s.charAt(left);
            char rightChar = s.charAt(right);
            while (!Character.isLetterOrDigit(leftChar) && left < right) {
                left++;
                leftChar = s.charAt(left);
            }
            while (!Character.isLetterOrDigit(rightChar) && left < right) {
                right--;
                rightChar = s.charAt(right);
            }
            if (Character.toLowerCase(leftChar) != Character.toLowerCase(rightChar)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
