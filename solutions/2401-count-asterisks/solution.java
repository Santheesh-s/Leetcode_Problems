class Solution {
    public int countAsterisks(String s) {
        int c=0,star=0;
        for(char i:s.toCharArray()){
            if((c&1)==0)
                if(i=='*')
                    star+=1;
            if(i=='|')
                    c+=1;
        }
        return star;
    }
}
