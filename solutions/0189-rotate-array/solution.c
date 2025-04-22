void rotate(int* nums, int numsSize, int k) {
        int m=0,n=numsSize;
        k=k%n;
        int arr[n];
        for(int i=n-k;i<n;i++)
            arr[m++]=nums[i];
        for(int i=0;i<n-k;i++)
            arr[m++]=nums[i];
        for(int i=0;i<n;i++)
            nums[i]=arr[i];
}
