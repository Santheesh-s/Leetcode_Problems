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
class Solution {
    List<Integer>ls=new ArrayList<>();
    public void flatten(TreeNode root) {
        preorder(root);
        TreeNode temp=root;
        int n=ls.size(),i=1;
        if(root==null) return;
        while(i<n)
        {
            temp.left=null;
            temp.right=new TreeNode(ls.get(i));
            temp=temp.right;
            i++;
        }        
    }
    public void preorder(TreeNode root)
    {
        if(root==null)
            return ;
        ls.add(root.val);
        preorder(root.left);
        preorder(root.right);
    }
}
