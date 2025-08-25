class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int a=0;
        for(int b:derived)
            a^=b;
        if(a==0)
            return true;
        return false;
    }
}
