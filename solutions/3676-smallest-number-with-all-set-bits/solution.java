class Solution {
    public int smallestNumber(int n) {
        int i=0,a=0;
    while(n>0)
    {
        i+=Math.pow(2,a++);
        n>>=1;
    }
    return i;
    }
}
