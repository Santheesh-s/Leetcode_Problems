class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int n=numOnes+numZeros+numNegOnes;
        int i,sum=0;
        int m=numOnes+numZeros;
        int[] arr=new int[n];
        for(i=0;i<numOnes;i++)
            arr[i]=1;
        for(i=numOnes;i<m;i++)
            arr[i]=0;
        for(i=m;i<n;i++)
            arr[i]=-1;
        for(i=0;i<k;i++)
            sum+=arr[i];
        return sum;
    }
}
