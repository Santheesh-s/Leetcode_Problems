class Solution {
    public int countSeniors(String[] details) {
        int count=0;
        for(String a:details)
            if(Integer.parseInt(a.substring(11,13))>60)
                count++;
        return count;
    }
}
