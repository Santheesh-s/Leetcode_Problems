class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        Set<Integer>ls1=new HashSet<>();
        Set<Integer>ls2=new HashSet<>();
        for (int num : nums1) ls1.add(num);
        for (int num : nums2) ls2.add(num);
        int c=0,d=0;
        for(int a:nums1)
            if(ls2.contains(a))
                c++;
        for(int a:nums2)
            if(ls1.contains(a))
                d++;
        return new int[]{c,d};
    }
}
