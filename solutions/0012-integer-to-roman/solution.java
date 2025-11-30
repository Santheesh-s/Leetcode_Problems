class Solution {
    private static final int[] arr={1000,900,500,400,100,90,50,40,10,9,5,4,1};
    private static String[] brr={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        
    public static String intToRoman(int num) {
        int i=0;
        String s="";
        while(num>0)
        {
            if(num-arr[i]>=0)
            {
                s+=brr[i];
                num-=arr[i];
            }
            else i++;
        }
        return s;
    }
}
