int findMin(int* nums, int numsSize) {
    int l=0,r=numsSize-1;
    if(nums[l]<nums[r]) return nums[l];
    int min = nums[0];

    while (l <= r) {
        if (nums[l] < min)
            min = nums[l];
        if (nums[r] < min)
            min = nums[r];

        l++;
        r--;
    }

    return min;
}
