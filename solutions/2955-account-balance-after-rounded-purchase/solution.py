class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        p=purchaseAmount%10;
        if(p>=5):
            purchaseAmount+=(10-p);
        else:
            purchaseAmount-=p;
        return 100-purchaseAmount;
