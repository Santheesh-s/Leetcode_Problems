class Solution {
    public boolean areOccurrencesEqual(String s) {
        Set<Character>ls=new HashSet<>();
        List<Character>ls2=new ArrayList<>();
        for(char a:s.toCharArray())
        {
            ls.add(a);
            ls2.add(a);
        }
        int n=Collections.frequency(ls2,s.charAt(0));
        for(char i:ls)
            if(Collections.frequency(ls2,i)!=n)
                return false;
        return true;
    }
}
