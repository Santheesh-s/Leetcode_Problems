/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
    let count=0,r=x^y;
    while(r>0)
    {
        if(r&1)
            count++;
        r>>=1;
    }
    return count;
};
