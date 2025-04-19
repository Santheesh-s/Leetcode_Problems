int minCostToMoveChips(int* position, int positionSize) {
    int e=0,o=0;
    for(int i=0;i<positionSize;i++)
    {
        if((*(position+i)&1))
            o++;
        else
            e++;
    }
    return o<e?o:e;
}
