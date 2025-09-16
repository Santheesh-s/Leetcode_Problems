class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Set<Integer>ls=new HashSet<>();
        Map<Integer,Integer> map=new HashMap<>();
        int n=nums.length;
        int max=Integer.MIN_VALUE;
        for(int i:nums)
        {
            map.put(i,map.getOrDefault(i,0)+1);
            if(map.get(i)>n/3)
                ls.add(i);
            if(max<map.get(i))
                max=map.get(i);
        }
        for(int l:ls)
        {
            if(map.get(l)<=n/3)
                ls.remove(l);
        }
        return new ArrayList<>(ls);
    }
}
