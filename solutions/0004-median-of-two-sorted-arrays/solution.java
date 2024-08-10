class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int c=nums1.length+nums2.length;
        int merge[]=new int[c],k=0;

        for(int i=0;i<nums1.length;i++)
        {
            merge[k++]=nums1[i];
        }
        for(int i=0;i<nums2.length;i++)
        {
            merge[k++]=nums2[i];
        }

        Arrays.sort(merge);

        if(k%2==0)
        {
            k=k/2;
            return (double)(merge[k]+merge[k-1])/2;
        }
        k=k/2;
        return (double)merge[k];
        
    }
}
