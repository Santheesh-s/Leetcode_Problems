class Solution {
    public int minOperations(String[] logs) {
        int c=0;
        for(String i:logs)
        {
            if(i.equals("../"))
            {
                c-=1;
                c=c<0?0:c;
            }
            else if(i.equals("./"))
                c=c;
            else
                c+=1;
        }
        return c;
    }
}
