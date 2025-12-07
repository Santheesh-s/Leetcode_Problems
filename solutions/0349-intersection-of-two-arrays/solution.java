class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Map<Integer,Integer>map=new HashMap<>();
        int n1=nums1.length,n2=nums2.length,k=0;
        
        int arr[]=new int[n1];
        for(int i=0;i<n1;i++)
            map.put(nums1[i],1);
        for(int i=0;i<n2;i++)
        {
            if (map.containsKey(nums2[i]) && map.get(nums2[i]) == 1) {
                arr[k++] = nums2[i];
                map.put(nums2[i], 0);
            }
        }   
        return Arrays.copyOf(arr, k);
    }
}
