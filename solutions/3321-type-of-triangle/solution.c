char* triangleType(int* nums, int numsSize) {
    if((*(nums)+*(nums+1)>*(nums+2) &&  *(nums)+*(nums+2)>*(nums+1) )&& *(nums+2)+*(nums+1)>*(nums))
    {
        if(*(nums)==*(nums+1) && *(nums)==*(nums+2))
            return "equilateral";
        else if(*(nums)==*(nums+1) || *(nums)==*(nums+2) ||*(nums+1)==*(nums+2) )
            return "isosceles";
        else if(*(nums)!=*(nums+1) || *(nums)!=*(nums+2))
            return "scalene";
    }
    return "none";
}
