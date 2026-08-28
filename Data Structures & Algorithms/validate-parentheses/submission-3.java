class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = Map.of('{', '}', '(', ')', '[', ']');
        Stack<Character> openBrackets = new Stack<>();
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                openBrackets.push(c);
            } else if (openBrackets.size() > 0 && map.get(openBrackets.peek()).equals(c)) {
                openBrackets.pop();
            } else {
                return false;
            }
        }
        if (openBrackets.size() == 0) {
            return true;
        }
        return false;
    }
}
