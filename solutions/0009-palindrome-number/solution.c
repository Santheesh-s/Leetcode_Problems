bool reverse(char *arr)
{
    int l=0,r=strlen(arr)-1;
    while(l<r)
    {
        if(arr[l]!=arr[r])
            return false;
        l++;r--;
    }
    return true;
}
bool isPalindrome(int x) {
    char charArray[20]; 

    // Use snprintf for safety (specify buffer size)
    snprintf(charArray, sizeof(charArray), "%d", x); 

    return reverse(charArray);
}
