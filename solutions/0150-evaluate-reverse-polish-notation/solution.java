class Solution {
    public int evalRPN(String[] tokens) {
        int n =tokens.length;
        Stack<Integer> stk =new Stack<>();
        for(int i=0 ; i<n ;i++)
        {
            if(tokens[i].equals("+") || tokens[i].equals("-")|| tokens[i].equals("*") || tokens[i].equals("/"))
            {
                int b=stk.pop();
                int a=stk.pop();
                if(tokens[i].equals("+")) stk.push(a+b);
                if(tokens[i].equals("-")) stk.push(a-b);
                if(tokens[i].equals("*")) stk.push(a*b);
                if(tokens[i].equals("/")) stk.push(a/b);
            }
            else
               stk.push(Integer.parseInt(tokens[i]));
        }
        return stk.pop();
    }
}
