class Solution {
    public long interchangeableRectangles(int[][] rectangles) {
        long res=0;
        Map<Double,Long>map=new HashMap<>();
        for(int[] r:rectangles)
        {
            double ratio=(double)r[0]/r[1];
            res+=map.getOrDefault(ratio,0l);
            map.put(ratio,map.getOrDefault(ratio,0l)+1);
        }
        return res;
    }
}
