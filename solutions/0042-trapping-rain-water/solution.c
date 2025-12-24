int trap(int* height, int heightSize) {
    int left[heightSize];
    int right[heightSize];
    int max=0,sum=0;
    for(int i=0;i<heightSize;i++)
        left[i]=max=fmax(max,height[i]);
    max=0;
    for(int i=heightSize-1;i>=0;i--)
        right[i]=max=fmax(max,height[i]);
    for(int i=0;i<heightSize;i++)
        sum+=(fmin(left[i],right[i])-height[i]);
    return sum;
}
