class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        Map<Integer,Integer>map2=new HashMap<>();
        int[] arr=new int[A.length];
        for(int i=0;i<A.length;i++)
        {
            arr[i]=0;
            map2.put(B[i],map2.getOrDefault(B[i],0)+1);
            for(int j=0;j<i+1;j++)
            {
                if(map2.containsKey(A[j]))
                    arr[i]++;
            }
        }
        return arr;
    }
}
