/**
 * @param {number} purchaseAmount
 * @return {number}
 */
var accountBalanceAfterPurchase = function(purchaseAmount) {
    var p=purchaseAmount%10;
        if(p>=5)
            purchaseAmount+=(10-p);
        else
            purchaseAmount-=p;
        return 100-purchaseAmount;
};
