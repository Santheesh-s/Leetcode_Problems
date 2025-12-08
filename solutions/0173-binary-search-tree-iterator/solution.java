/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class BSTIterator {
    List<Integer>ls=new ArrayList<>();
    int cur=0;
    int n=ls.size();
    public BSTIterator(TreeNode root) {
        inorder(root);
    }
    public void inorder(TreeNode root)
    {
        if(root==null) return ;

        inorder(root.left);
        ls.add(root.val);
        inorder(root.right);
    }
    public int next() {
        return ls.get(cur++);
    }
    
    public boolean hasNext() {
        return cur<ls.size();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
