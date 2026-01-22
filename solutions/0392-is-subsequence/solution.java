class Solution {
    public boolean isSubsequence(String s, String t) {
        char[] arr=s.toCharArray(),brr=t.toCharArray();
        int n=arr.length,j=0;
        for(char i:brr)
            if(j<n)
                if(i==arr[j])
                    j+=1;
        return (j==n)?true:false;
    }
}
