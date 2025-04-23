class Solution {
    public int search(int[] nums, int target) {
        return BinarySearch(nums,target,0,nums.length-1);
    }

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
}
