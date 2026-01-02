class Solution {
    public String addSpaces(String s, int[] spaces) {
        Set<Integer>set=new HashSet<>();
        StringBuilder res=new StringBuilder();

        for(int i=0;i<spaces.length;i++)
            set.add(spaces[i]);
        for(int i=0;i<s.length();i++)
        {
            if(set.contains(i))
                res.append(" ");
            res.append(s.charAt(i));
        }
        return res.toString();
    }
}
