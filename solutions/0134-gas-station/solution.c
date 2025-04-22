int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize) {
    int a=0,b=0,n=0,gain=0;
        for(int i=0;i<gasSize;i++)
        {
            gain+=gas[i]-cost[i];
            if(gain<0)
            {
                n=i+1;
                gain=0;
            }
            a+=gas[i];
            b+=cost[i];
        }
        if(a>=b)
            return n;
        return -1;
}
