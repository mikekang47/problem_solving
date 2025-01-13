import java.util.*;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < magazine.length(); i++) {
            char key = magazine.charAt(i);
            if(map.containsKey(key)) {
                map.put(key, map.get(key) + 1);
            } else {
                map.put(key, 1);
            }
        }
        for(int i = 0; i < ransomNote.length(); i++) {
            char key = ransomNote.charAt(i);
            if(map.containsKey(key)) {
                if(map.get(key) <= 0) {
                    return false;
                } else {
                    map.put(key, map.get(key) -1);
                }
            } else {
                return false;
            }
        }
        return true;
    }
}