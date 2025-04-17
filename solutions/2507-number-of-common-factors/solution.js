/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var commonFactors = function(a, b) {
    var n=0;
        for(let i=1;i<=b;i++)
            if(a%i==0 && b%i==0)
                n++;
        return n;
};
