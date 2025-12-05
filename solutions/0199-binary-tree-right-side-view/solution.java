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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer>ls=new ArrayList<>();
        Queue<TreeNode>q=new LinkedList<>();
        int size=0;
        if(root==null) return ls;
        q.offer(root);
        while(!q.isEmpty())
        {
            size=q.size();
            while(size>0)
            {
                TreeNode temp=q.poll();
                if(size==1)
                    ls.add(temp.val);
                if(temp.left!=null) q.offer(temp.left);
                if(temp.right!=null) q.offer(temp.right);
                size-=1;
            }
        }
        return ls;
    }
}
