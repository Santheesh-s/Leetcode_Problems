class Solution {
    public int bitwiseComplement(int n) {
        String s="";
        for(char i:Integer.toBinaryString(n).toCharArray())
            if(i=='0')
                s+='1';
            else
                s+='0';
        return Integer.parseInt(s,2);
    }
}
