class Solution {
    public String removeOuterParentheses(String s) {
        int count=0;
        String str="";
        for(int i=0;i<s.length();i++)
        {
            if(s.charAt(i) =='(' && count++ !=0) str=str+'(';
             if(s.charAt(i) ==')' && --count!=0) str=str+')';
        }
        return str;
    }
}
