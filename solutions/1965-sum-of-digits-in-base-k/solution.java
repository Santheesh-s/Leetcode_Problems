class Solution {
    public int sumBase(int n, int k) {
        String a=Integer.toString(n,k);
        int ac=Integer.parseInt(a);
        int sum=0;
        while(ac!=0)
        {
            sum+=ac%10;
            ac=ac/10;
        }
        return sum;
    }
}
