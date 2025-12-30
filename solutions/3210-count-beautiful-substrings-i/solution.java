class Solution {
    public int beautifulSubstrings(String s, int k) {
        int n=s.length(),count=0;
        for(int i=0;i<n;i++)
        {
            int v=0,c=0;
            for(int j=i;j<n;j++)
            {
                if("aeiou".indexOf(s.charAt(j))!=-1)
                    v++;
                else
                    c++;
                if( v==c && (v*c)%k==0)
                    count++;
            }
        }
        return count;
    }
}
