/**
 * @param {number} n
 * @return {number}
 */
var sumOfMultiples = function(n) {
    var m=0;
        for(let i=0;i<=n;i++)
            if(i%3==0 || i%5==0 || i%7==0)
                m+=i;
        return m;
};
