/**
 * @param {number} n
 * @return {boolean}
 */
var isThree = function(n) {
    var c=0;
        for(let i=1;i<=n;i++)
        {
            if(n%i==0)
                c++;
        }
        if(c==3)
            return true;
        return false;
};
