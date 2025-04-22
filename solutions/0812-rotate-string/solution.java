class Solution {
    public boolean rotateString(String s, String goal) {
    /*    List<String>ls=new ArrayList<>();
        for(char a:s.toCharArray())
            ls.add(a+"");
        String a=String.join("",ls);
        Collections.rotate(ls,1);
        while(a.equals(String.join("",ls)))
        {
            System.out.print(ls);
            if(goal.equals(String.join("",ls)))
                return true;
            Collections.rotate(ls,1);
        }
        return false;*/
        if(s.length()==goal.length())
            if((s+s).contains(goal))
                return true;
        return false;
    }
}
