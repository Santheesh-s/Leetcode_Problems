class Solution {
    public int numberOfSpecialChars(String word) {
        Set<Character>ls=new HashSet<>();
        int count=0;
        for(char a:word.toCharArray())
            ls.add(a);
        for(char a:ls)
            if(word.indexOf(a-32)!=-1)
                count++;
        return count;
    }
}
