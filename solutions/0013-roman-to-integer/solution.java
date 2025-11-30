class Solution {
static final Map<String,Integer> mp = new HashMap<>();

    static {
        mp.put("M", 1000);
        mp.put("D", 500);
        mp.put("C", 100);
        mp.put("L", 50);
        mp.put("X", 10);
        mp.put("V", 5);
        mp.put("I", 1);
    }
        private int max=-1,sum=0,i,val;
    public int romanToInt(String s) {    
        for(i=s.length()-1;i>=0;i--)
        {
            val=mp.get(String.valueOf(s.charAt(i)));
            max=Math.max(max,val);
            if(val>=max) sum+=val;
            else sum-=val;
        }
        return sum;
    }
}
