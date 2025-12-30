int maxChunksToSorted(int* arr, int arrSize) {
    int res=0,diff=0;
    for(int i=0;i<arrSize;i++)
    {
        diff+=arr[i]-i;
        res += diff == 0;
    }
    return res;
}
