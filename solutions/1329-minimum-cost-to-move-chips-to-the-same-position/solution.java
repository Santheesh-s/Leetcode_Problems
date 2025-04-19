class Solution {
    public int minCostToMoveChips(int[] position) {
    int e=0,o=0;
    for(int i=0;i<position.length;i++)
    {
        if((position[i]&1)==1)
            o++;
        else
            e++;
    }
    return o<e?o:e;
    }
}
