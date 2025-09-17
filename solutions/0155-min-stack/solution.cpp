class MinStack {
public:
    vector<pair<int ,int>>s;
    int tp=-1;
    int mn;
    MinStack() {
        
    }
    
    void push(int val) {
        if(tp == -1)
            mn=val;
        else
            mn=min(s[tp].second,val);
        tp++;
        s.push_back({val,mn});
        
    }
    
    void pop() {
        tp--;
        s.pop_back();
    }
    
    int top() {
        return s.back().first;
        
    }
    
    int getMin() {
        return s.back().second;
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
