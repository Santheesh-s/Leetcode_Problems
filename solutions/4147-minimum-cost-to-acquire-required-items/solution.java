class Solution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long min = Math.min(need1, need2);
        long max = Math.max(need1, need2);

        long withOnlyCostBoth = max * costBoth;

        long withCostBoth = min * costBoth
                          + (need1 - min) * cost1
                          + (need2 - min) * cost2;

        long withoutCostBoth = (long) need1 * cost1
                             + (long) need2 * cost2;

        return Math.min(withOnlyCostBoth,
               Math.min(withCostBoth, withoutCostBoth));
    }
}

