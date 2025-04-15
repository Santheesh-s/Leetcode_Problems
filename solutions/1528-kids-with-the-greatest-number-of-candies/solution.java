class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int n=0;
        List<Boolean>ls=new ArrayList<>();
        for(int i:candies)
            if(i>n)
                n=i;
        for(int i:candies)
        {
            if((i+extraCandies)>=n)
                ls.add(true);
            else
                ls.add(false);
        }
        return ls;
    }
}
