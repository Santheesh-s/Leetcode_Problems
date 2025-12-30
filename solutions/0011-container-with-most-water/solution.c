int maxArea(int* height, int heightSize) {
    int l=0,r=heightSize-1;
    int a,b,res=0;
    while(l<r)
    {
        a=height[l];
        b=height[r];
        int c=fmin(a,b);
        int area=(r-l)*c;
        if( area>res )
            res=area;
        if(c==a)
            l++;
        else
            r--;
    }
    return res;
}
