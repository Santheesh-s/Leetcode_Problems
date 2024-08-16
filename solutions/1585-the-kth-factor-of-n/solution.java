class Solution {
    public int kthFactor(int n, int k) {
        int arr[]=new int[n],kt=0;
        for(int i=1;i<=n;i++)
        {
            if(n%i==0)
            {
                arr[kt++]=i;
            }
        }
        if(k>kt)return -1;
        return arr[k-1];
    }
}
