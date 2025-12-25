class Solution {
    public boolean isValid(String st) {
        Stack<Character>s=new Stack<>();
        for(char a:st.toCharArray())
        {
            if(a=='{' || a=='[' || a=='(')
                s.push(a);
            else
            {
                if(s.isEmpty()) return false;
                if(a=='}' && s.pop()!='{') return false;
                if(a==']' && s.pop()!='[') return false;
                if(a==')' && s.pop()!='(') return false;
            }
        }
        return s.isEmpty();
    }
}
