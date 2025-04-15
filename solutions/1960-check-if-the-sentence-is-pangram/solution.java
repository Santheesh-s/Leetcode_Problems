class Solution {
    public boolean checkIfPangram(String sentence) {
        int n=sentence.length();
        if(n<26)
            return false;
        Set<Character>ls=new HashSet<>();
        for(char s:sentence.toCharArray())
            ls.add(s);
        if(ls.size()!=26)
            return false;
        return true;
    }
}
