class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer>s=new Stack<>();
        for(String a:tokens)
        {
            if(a.equals("+") )
                s.push(s.pop()+s.pop());
            else if(a.equals("-") )
            {
                int x=s.pop();
                int y=s.pop();
                s.push(y-x);
            }
            else if(a.equals("*") )
                s.push(s.pop()*s.pop());
            else if(a.equals("/") )
            {
                int x=s.pop();
                int y=s.pop();
                s.push(y/x);
            }
            else
                s.push(Integer.parseInt(a));
        }
        return s.pop();
    }
}
