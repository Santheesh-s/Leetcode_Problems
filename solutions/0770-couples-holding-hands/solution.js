/**
 * @param {number[]} row
 * @return {number}
 */
var minSwapsCouples = function(row) {
    let first=0,second=0,temp,count=0;
    for(let i=0;i<row.length;i+=2)
    {
        first=row[i];
        second=row[i]^1;
        if(row[i+1]==second)
            continue;
        for(let j=i+1;j<row.length;j++)
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
};
