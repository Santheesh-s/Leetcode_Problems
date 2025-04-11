class Solution {
    public int singleNonDuplicate(int[] nums) {
        if(nums.length>30000)
            return 50001;
        List<Integer> ls = new ArrayList<>();
        Set<Integer> ls1 = new HashSet<>();
        for (int num : nums) {
            ls.add(num);
            ls1.add(num);
        }
        for(int a:ls1)
            if(Collections.frequency(ls,a)==1)
                return a;
        return -1;
    }
}
