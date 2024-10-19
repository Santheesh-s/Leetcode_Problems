class Solution {
    public int minimizedStringLength(String s) {
        Set<Character>unique=new HashSet<>();
        for(int i=0;i<s.length();i++)
            unique.add(s.charAt(i));
        return unique.size();
    }
}
