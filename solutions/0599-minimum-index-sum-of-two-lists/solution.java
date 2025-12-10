class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        String[] a=new String[list1.length];
        int k=0,m=Integer.MAX_VALUE;
        int n=list1.length,n2=list2.length;
        Map<String,Integer>map=new HashMap<>();
        for(int i=0;i<n;i++)
            map.put(list1[i],i);
        for(int i=0;i<n2;i++)
            if(map.containsKey(list2[i]))
                m=Math.min(m,map.get(list2[i])+i);
        for(int i=0;i<n2;i++)
            if(map.containsKey(list2[i]) && map.get(list2[i])+i==m)
                a[k++]=list2[i];
        return Arrays.copyOf(a,k);

    }
}
