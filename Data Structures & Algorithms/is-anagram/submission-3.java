class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> hashmap = new HashMap<>();
        for (char c : s.toCharArray()) {
            hashmap.put(c, hashmap.getOrDefault(c, 0) + 1);
        }
        for (char c : t.toCharArray()) {
            if (!hashmap.containsKey(c)) {
                return false;
            }
            hashmap.put(c, hashmap.get(c) - 1);
            hashmap.remove(c, 0);
        }
        if (hashmap.size() == 0) {
            return true;
        }
        return false;
    }
}
