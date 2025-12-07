/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        Queue<Node>q=new LinkedList<>();
        if(root==null) return root;
        q.offer(root);
        while(!q.isEmpty())
        {
            int size=q.size();
            List<Node>ls=new ArrayList<>();
            while(size-- >0)
            {
                Node temp=q.poll();
                ls.add(temp);
                if(temp.left!=null)
                    q.offer(temp.left);
                if(temp.right!=null)
                    q.offer(temp.right);
            }
            if(ls.size()==1)ls.get(0).next=null;
            int i;
            for(i=1;i<ls.size();i++)
                ls.get(i-1).next=ls.get(i);
            ls.get(i-1).next=null;
        }
        return root;
    }
}
