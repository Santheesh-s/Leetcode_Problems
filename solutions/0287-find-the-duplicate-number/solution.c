int findDuplicate(int* nums, int numsSize) {
    int arr[numsSize+1]={};
    for(int i=0;i<numsSize;i++)
    {
        if(arr[nums[i]])
            return nums[i];
        arr[nums[i]]=1;
    }
    return 0;
}
