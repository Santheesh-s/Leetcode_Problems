/**
 * @param {number} n
 * @return {boolean}
 */
var hasAlternatingBits = function(n) {
    let count=n&1;
    n>>=1;
    while(n>0)
    {
        if((n&1)==count)
            return false;
        count=(n&1);
        n>>=1;
    }
    return true;
};
