class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        String a="",b="",c="";
        for(char s:firstWord.toCharArray())
            a+=s-97;
        for(char s:secondWord.toCharArray())
            b+=s-97;
        for(char s:targetWord.toCharArray())
            c+=s-97;
        return (Integer.parseInt(a)+Integer.parseInt(b))==Integer.parseInt(c);
    }
}
