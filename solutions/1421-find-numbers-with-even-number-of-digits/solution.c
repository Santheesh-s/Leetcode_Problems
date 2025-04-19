int findNumbers(int* nums, int numsSize) {
    int ev=0;
    for(int i=0;i<numsSize;i++)
    {
        int a=0;
        while(nums[i]!=0)
        {
            nums[i]/=10;
            a++;
        }
        if(a%2==0)
            ev++;
    }
    return ev;
}
