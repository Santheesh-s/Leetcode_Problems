/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    if(n==1)
        return true;
    let count=0;
    if(n>0 && (n&(n-1))==0)
    {
        while(n>0)
        {
            if((n&1)==0)
                count++;
            n>>=1;
        }
    }
    if(count!=0 && (count&1)==0)
        return true;
    return false;
};
