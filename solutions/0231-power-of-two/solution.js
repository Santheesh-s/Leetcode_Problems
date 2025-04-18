/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if(n>=1)
        {
            if((n&(n-1))==0)
                return true;
        }
        return false;
};
