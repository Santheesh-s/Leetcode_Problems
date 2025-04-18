bool isPalindrome(int x) {
    int temp=x;
    long int rev=0;
    if(x<0 || (x!=0 && x%10==0)) return false;
    while(x!=0)
    {
        rev=rev*10+x%10;
        x/=10;
    }
    if(rev==temp)
        return true;
    return false;
}
