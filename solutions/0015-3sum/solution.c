/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int compare(const void *a,const void *b)
{
    return *(int*)a-*(int *)b;
}
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int **arr=(int **)malloc(sizeof(int*)*20000);
    qsort(nums,numsSize,sizeof(int),compare);
    int l,r,j=0,sum;
    for(int i=0;i<numsSize-2;i++)
    {
        l=i+1;r=numsSize-1;
        if(i > 0 && nums[i] == nums[i-1]) continue;
        while(l<r)
        {
            sum=nums[i]+nums[l]+nums[r];
            if(sum==0)
            {
               arr[j]=(int*)malloc(sizeof(int)*3);
               arr[j][0]=nums[i];
               arr[j][1]=nums[l];
               arr[j][2]=nums[r];
               l++;r--;
               j++;
               while(l < r && nums[l] == nums[l-1]) l++;
               while(l < r && nums[r] == nums[r+1]) r--;
            }
            else if(sum<0)
                l++;
            else
                r--;
        }
    }
    *returnColumnSizes = (int*)malloc(sizeof(int) * j);
    for(int k = 0; k < j; k++)
        (*returnColumnSizes)[k] = 3;
    *returnSize=j;
    return arr;
}
