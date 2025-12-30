class Solution {
    public boolean checkPrimeFrequency(int[] nums) {
        List<Integer>ls=new ArrayList<>(List.of(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97));

        Map<Integer,Integer>map=new HashMap<>();
        for(int a:nums)
            map.put(a,map.getOrDefault(a,0)+1);
        for(int a:map.values())
            if(ls.contains(a))
                return true;
        return false;
    }
}
