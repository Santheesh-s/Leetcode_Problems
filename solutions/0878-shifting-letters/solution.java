class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        char[] arr= s.toCharArray();
        int sum=0,k=0;
        for(int i=arr.length-1;i>=0;i--)
        {
            sum+=(shifts[i]%26);
            arr[i]+=sum%26;
            if(arr[i]>122)
                arr[i]-=26;           
        }
        return new String(arr);
    }
}
