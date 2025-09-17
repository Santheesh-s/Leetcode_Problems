class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int n =tokens.size();
        stack<int> stk;
        for(int i=0 ; i<n ;i++)
        {
            if(tokens[i]=="+" || tokens[i]=="-"|| tokens[i]=="*" || tokens[i]=="/")
            {
                int b=stk.top();
                stk.pop();

                int a=stk.top();
                stk.pop();
                if(tokens[i]=="+") stk.push(a+b);
                if(tokens[i]=="-") stk.push(a-b);
                if(tokens[i]=="*") stk.push(a*b);
                if(tokens[i]=="/") stk.push(a/b);
            }
            else
               stk.push(stoi(tokens[i]));
        }
        return stk.top();
        
    }
};
