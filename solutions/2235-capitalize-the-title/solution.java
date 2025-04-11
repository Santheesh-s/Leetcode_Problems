class Solution {
    public String capitalizeTitle(String title) {
        String[] a=title.split("\\ ");
        for(int i=0;i<a.length;i++)
            if(a[i].length()<=2)
                a[i]=a[i].toLowerCase();
            else
                a[i]=a[i].substring(0,1).toUpperCase()+a[i].substring(1).toLowerCase();
        return String.join(" ",a);
    }

}
