/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceElements(int* arr, int arrSize, int* returnSize) {
    *returnSize=arrSize;
    for(int i=arrSize-1;i>0;i--)
        if(arr[i]>arr[i-1])
            arr[i-1]=arr[i];
    for(int i=1;i<arrSize;i++)
        arr[i-1]=arr[i];
    arr[arrSize-1]=-1;
    return arr;
}
