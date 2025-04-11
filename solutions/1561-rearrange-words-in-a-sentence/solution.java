class Solution {
    public String arrangeWords(String text) {
        List<String>ls=new ArrayList<>(Arrays.asList(text.split("\\ ")));
        ls.sort(Comparator.comparingInt(String::length));
        String a=String.join(" ",ls).toLowerCase();
        return a.substring(0,1).toUpperCase()+a.substring(1);
    }
}
