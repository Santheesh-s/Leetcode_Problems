class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer>ls=new ArrayList<>();
        ls.add(0);
        for (int i = 1; i < (1 << n); i++) 
        {
            ls.add(i ^ (i >> 1));
        }
        return ls;
    }
}
