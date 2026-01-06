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
    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode>q=new LinkedList<>();
        if(root==null) return 0;
        int sum=-1000000,i=0,res=0;
        q.offer(root);
        while(!q.isEmpty())
        {
            int size=q.size(),sum1=0;i++;
            while(size-- >0)
            {
                TreeNode temp=q.poll();
                sum1+=temp.val;
                if(temp.left!=null)
                    q.offer(temp.left);
                if(temp.right!=null)
                    q.offer(temp.right);
            }
            if(sum<sum1)
            {
                sum=sum1;
                res=i;
            }
        }
        return res;
    }
}
