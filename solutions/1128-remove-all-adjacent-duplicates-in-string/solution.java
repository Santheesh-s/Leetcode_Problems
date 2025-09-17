class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stk = new Stack<>();
        int len =s.length();
        for(int i=0;i<len;i++)
        {
            boolean destroy = false;
            while(!stk.isEmpty() && stk.peek()==s.charAt(i))
            {
                stk.pop();
                destroy = true;
            }
            if(!destroy)
                stk.push(s.charAt(i));
        }
        String str = "";
        //System.out.println(stk);
        for(int i=0;i<stk.size();i++)
        {
             str += stk.get(i); 
        }
    return str;
    }
}
