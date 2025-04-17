class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        int p=purchaseAmount%10;
        if(p>=5)
            purchaseAmount+=(10-p);
        else
            purchaseAmount-=p;
        return 100-purchaseAmount;
    }
}
