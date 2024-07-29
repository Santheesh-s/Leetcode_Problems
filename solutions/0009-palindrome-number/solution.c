bool isPalindrome(int x) {
    if(x<0)
    {
        return false;
    }
    else
    {
        int n=x,rem,rev=0;
        while(n!=0)
        {
            rem=n%10;
            n=n/10;
        if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && rem > INT_MAX % 10)) {
            return 0; // Overflow, return 0
        }
        if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && rem < INT_MIN % 10)) {
            return 0; // Underflow, return 0
        }
        
         rev=rev*10+rem;
        }
        if(rev==x)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
