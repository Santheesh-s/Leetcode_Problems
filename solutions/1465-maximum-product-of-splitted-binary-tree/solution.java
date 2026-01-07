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
    int MOD=(int)Math.pow(10,9)+7;

    long maxProduct,total;
    public long sum(TreeNode root)
    {
        if(root==null)  return 0;
        return root.val+sum(root.left)+sum(root.right);
    }
    public int maxProduct(TreeNode root) {
        if(root==null) return 0;
        maxProduct=0;
        total=sum(root);
        dfsMax(root);
        return (int)( maxProduct % MOD);
    }
    public long dfsMax(TreeNode root)
    {
        if(root==null) return 0;

        long left=dfsMax(root.left);
        long right=dfsMax(root.right);

        long subtree=root.val+right+left;
        maxProduct=Math.max(maxProduct,subtree * (total-subtree));
        return subtree;
    }
}
