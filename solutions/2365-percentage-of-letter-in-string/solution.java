class Solution {
    public int percentageLetter(String s, char letter) {
        int n=0;
        for(char a:s.toCharArray())
            if(a==letter)
                n++;
        return (n*100)/s.length();
    }
}
