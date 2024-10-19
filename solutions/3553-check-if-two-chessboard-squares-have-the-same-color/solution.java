class Solution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        int row1=coordinate1.charAt(0)-'a'+1;
        int col1= Character.getNumericValue(coordinate1.charAt(1));
        int row2=coordinate2.charAt(0)-'a'+1;
        int col2= Character.getNumericValue(coordinate2.charAt(1));
        return (col1 + row1) % 2 == (col2 + row2) % 2;
    }
}
