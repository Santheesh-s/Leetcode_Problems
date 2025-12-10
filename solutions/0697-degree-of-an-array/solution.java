class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer,ArrayList> map=new HashMap<>();
        int m=-1;
        for(int i=0;i<nums.length;i++)
        {
            map.putIfAbsent(nums[i], new ArrayList<String>());
            map.get(nums[i]).add(i);
            m=Math.max(m,map.get(nums[i]).size());
        }
        int shortsub=Integer.MAX_VALUE;
        for(Map.Entry<Integer,ArrayList>entry:map.entrySet())
        {
            ArrayList<Integer> list = entry.getValue();
            int n=list.size();
            if(n==m)
            {
                int s = list.get(n - 1) - list.get(0) + 1;
                shortsub=Math.min(shortsub,s);
            }
        }
        return shortsub;
    }
}
