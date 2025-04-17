/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    var a=0,b=1,c=0;
    for(let i=0;i<n+1;i++)
    {
        c=a+b;
        a=b;b=c;
    }
    return a;
};
