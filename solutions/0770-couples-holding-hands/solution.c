int minSwapsCouples(int* row, int rowSize) {
    int first=0,second=0,temp,count=0;
    for(int i=0;i<rowSize;i+=2)
    {
        first=row[i];
        second=row[i]^1;
        if(row[i+1]==second)
            continue;
        for(int j=i+1;j<rowSize;j++)
        {
            if(second==row[j])
            {
                temp=row[i+1];
                row[i+1]=row[j];
                row[j]=temp;
                count++;
                break;
            }
        }
    }
    return count;
}
