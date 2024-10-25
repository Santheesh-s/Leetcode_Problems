import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isFascinating(int n) {
        String s = String.valueOf(n) + String.valueOf(n * 2) + String.valueOf(n * 3);
        System.out.println(s);
        Set<Character> digits = new HashSet<>();
        for (char ch : s.toCharArray()) {
            if (ch == '0' || !digits.add(ch)) { 
                return false;
            }
        }
        return digits.size() == 9;
    }
}

