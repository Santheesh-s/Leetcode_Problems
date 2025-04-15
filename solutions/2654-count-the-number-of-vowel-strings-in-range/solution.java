class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        int count=0;
        for(int i=left;i<=right;i++)
        {
            char a=words[i].charAt(0);
            char b=words[i].charAt(words[i].length()-1);
            if((a+"").matches("[aeiou]+") && (b+"").matches("[aeiou]+"))
                count++;
        }
        return count;
    }
}
