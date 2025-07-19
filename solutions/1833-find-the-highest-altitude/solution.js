/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let ans=0,sum=0,n=0;
    for(let i=0;i<gain.length;i++)
    {
        sum=ans+gain[i]+sum;
        if(n<sum)
            n=sum;
    }
    return n;
};
