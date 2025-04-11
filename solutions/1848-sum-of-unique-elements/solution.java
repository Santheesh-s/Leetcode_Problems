class Solution {
    public int sumOfUnique(int[] nums) {
        Set<Integer>ls=new HashSet<>();
        List<Integer>ls1=new ArrayList<>();
        int count,sum=0;
        for(int n:nums)
            ls.add(n);
        for(int n:ls)
        {
            count=0;
            for(int m:nums)
                if(n==m)
                    count+=1;
            if(count==1)
                ls1.add(n);
        }
        for(int m:ls1)
            sum+=m;
        return sum;
    }
}
