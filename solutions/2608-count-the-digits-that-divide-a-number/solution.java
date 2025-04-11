class Solution {
    public int countDigits(int num) {
        int count=0;
        for(char a:String.valueOf(num).toCharArray())
            if(num%Integer.parseInt(""+a)==0)
                count++;
        return count;
    }
}
