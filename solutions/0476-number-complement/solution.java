class Solution {
    public int findComplement(int num) {
        String b="";
        for(char i: Integer.toBinaryString(num).toCharArray())
            if (i=='0')
                b+='1';
            else
                b+='0';
        return Integer.parseInt(b,2);
    }
}
