class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer>set1=new HashSet<>();
        Set<Integer>set2=new HashSet<>();
        for(int n:nums1)
            set1.add(n);
        for(int n:nums2)
            set2.add(n);
        List<List<Integer>> ls=new ArrayList<List<Integer>>();
        List<Integer>ls1=new ArrayList<>();
        List<Integer>ls2=new ArrayList<>();
        for(int num:set1)
        {
            if(!set2.contains(num))
            {
                ls1.add(num);
            }
        }
        for(int num:set2)
        {
            if(!set1.contains(num))
            {
                ls2.add(num);
            }
        }
        ls.add(ls1);
        ls.add(ls2);
        return ls;
    }
}
