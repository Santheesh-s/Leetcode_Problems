int reverse(int x){
    int rem,rev=0;
        while (x != 0) {
        rem = x % 10;
        x = x / 10;
        
        // Check for overflow before updating rev
        if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && rem > INT_MAX % 10)) {
            return 0; // Overflow, return 0
        }
        if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && rem < INT_MIN % 10)) {
            return 0; // Underflow, return 0
        }
        
        rev = rev * 10 + rem;
    }
    return rev;
}
