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
    List<Double> ls=new ArrayList<>();
    public List<Double> averageOfLevels(TreeNode root) {
        avg(root);
        return ls;
    }
    public void avg(TreeNode root)
    {
        if(root==null) return ;
        Queue<TreeNode> q=new LinkedList<>();
        q.offer(root);
        int size=0;
        while(!q.isEmpty())
        {
            int s=0;
            long sum = 0L;  
            size=q.size();
            while(size-- >0)
            {
                TreeNode temp=q.poll();
                s+=1;
                sum+=temp.val;
                if(temp.left!=null)
                    q.offer(temp.left);
                if(temp.right!=null)
                    q.offer(temp.right);
            }
            ls.add(sum* 1.0/s+sum*0.0);
        }
    }
}
