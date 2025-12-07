class Solution {
    public boolean backspaceCompare(String s, String t) {
        StringBuilder sc=new StringBuilder();
        for(char a:s.toCharArray())
        {
            if(a!='#')
                sc.append(a);
            else if(sc.length()>=1)
                sc.deleteCharAt(sc.length() - 1);
        }
        StringBuilder sc1=new StringBuilder();
        for(char a:t.toCharArray())
        {
            if(a!='#')
                sc1.append(a);
            else if(sc1.length()>=1)
                sc1.deleteCharAt(sc1.length() - 1);
        }
        return sc1.toString().equals(sc.toString());
    }
}
