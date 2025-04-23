int search(int* nums, int numsSize, int target) {

int BinarySearch(int arr[],int target,int start,int end)
{
    if(start>end)
        return -1;
    
    int mid=(start+end)/2;
    if(arr[mid]==target)
        return mid;
    else if(target<arr[mid])
        return BinarySearch(arr,target,start,mid-1);
    else
        return BinarySearch(arr,target,mid+1,end);
}

    return BinarySearch(nums,target,0,numsSize-1);
}

