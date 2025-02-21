class Solution {
    public int maxPower(String s) {
        int max1=0,max=0;
        for(int i=0;i<s.length()-1;i++)
        {
            if(s.charAt(i)==s.charAt(i+1))
            {
                max1++;
                if(max1>max)
                    max=max1;
            }
            else
            {
                max1=0;
            }
        }
        return max+1;
    }
}
