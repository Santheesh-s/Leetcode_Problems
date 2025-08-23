/**
 * @param {number} n
 * @return {number}
 */
var consecutiveNumbersSum = function(n) {
    let count=0,i=1;
    while(n>0)
    {
        n=n-i;
        if(n%i==0)
            count++;
        i++;
    }
    return count;
};
