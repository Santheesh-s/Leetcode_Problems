class Solution {
public:
    bool isValid(string st) {
        stack<int> s;
        for(char a:st)
        {
            if(a=='(' || a=='[' || a=='{')
                s.push(a);
            else
            {
                if(s.empty()) return false;
                if(a=='}' && '{'!=s.top())
                    return false;
                if(a==']' && '['!=s.top())
                    return false;
                if(a==')' && '('!=s.top())
                    return false;
                s.pop();
            }
        }
        return s.empty();
    }
};
