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
    public int sumOfLeftLeaves(TreeNode root) {
        if(root==null) return 0;
        int res=0;
        Queue<TreeNode>q=new LinkedList<>();
        q.offer(root);
        while(!q.isEmpty())
        {
            int size=q.size();
            while(size-->0)
            {
                TreeNode temp=q.poll();
                if (temp.left != null)
                {
                    if (temp.left.left == null && temp.left.right == null)
                        res += temp.left.val;
                    else
                        q.offer(temp.left);
                }
                if(temp.right!=null)
                    q.offer(temp.right);
            }
        }
        return res;

    }
}
