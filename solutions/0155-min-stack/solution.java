class MinStack {
    Stack<Integer>s;
    int a=Integer.MAX_VALUE;
    public MinStack() {
        s=new Stack<>();
    }
    
    public void push(int val) {
        if (val <= a) {
            s.push(a);
            a = val;
        }
        s.push(val);
    }
    
    public void pop() {
        if (s.pop() == a)
            a = s.pop(); 
    }
    
    public int top() {
        return s.peek();
    }
    
    public int getMin() {
        return a;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
