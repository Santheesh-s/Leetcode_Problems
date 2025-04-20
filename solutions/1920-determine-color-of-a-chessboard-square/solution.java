class Solution {
    public boolean squareIsWhite(String coordinates) {
        boolean a=coordinates.charAt(0)%2==0;
        boolean b=coordinates.charAt(1)%2==0;
        if(a && b)
            return false;
        else if(!a && !b)
            return false;
        else if(a && !b)
            return true;
        return true;
    }
}
