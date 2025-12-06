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
    public TreeNode invertTree(TreeNode root) {
        return change(root);
    }
    public TreeNode change(TreeNode root)
    {
        Queue<TreeNode> q=new LinkedList<>();
        if(root==null) return root;
        q.offer(root);
        while(!q.isEmpty())
        {
            int size=q.size();
            while(size-- >0)
            {
                TreeNode temp=q.poll();
                TreeNode swap=temp.left;
                temp.left=temp.right;
                temp.right=swap;
                if(temp.left!=null)
                    q.offer(temp.left);
                if(temp.right!=null)
                    q.offer(temp.right);
            }
        }
        return root;
    }
}
