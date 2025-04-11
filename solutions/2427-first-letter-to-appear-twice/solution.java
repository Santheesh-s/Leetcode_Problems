class Solution {
    public char repeatedCharacter(String s) {
        List<Character> ls=new ArrayList<>();
        for(char a:s.toCharArray())
        {
            if(ls.contains(a))
                return a;
            ls.add(a);
        }
        return 'a';
    }
}
