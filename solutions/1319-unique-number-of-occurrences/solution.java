class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer,Integer>map=new HashMap<>();
        Set<Integer>set=new HashSet<>();
        int n=arr.length;
        for(int i=0;i<n;i++)
            map.put(arr[i],map.getOrDefault(arr[i],0)+1);
        for(int i : map.values())
            set.add(i);
        return map.size()==set.size();
    }
}
