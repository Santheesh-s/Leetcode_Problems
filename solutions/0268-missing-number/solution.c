int missingNumber(int* nums, int numsSize) {
    int n=(numsSize*(numsSize+1))/2,sum=0;
    for(int i=0;i<numsSize;i++)
        sum+=*(nums+i);
    return n-sum;
}
