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
    public boolean isCousins(TreeNode root, int x, int y) {
        Queue<TreeNode>q=new LinkedList<>();
        q.offer(root);
        while(!q.isEmpty())
        {
            int size=q.size();
            Set<Integer>s=new HashSet<>();
            while(size-- >0)
            {
                TreeNode temp=q.poll();
                if(temp.left!=null && temp.right!=null)
                    if((temp.left.val==x && temp.right.val==y) || (temp.left.val==y && temp.right.val==x)) return false;
                if(temp.left!=null)
                {
                    q.offer(temp.left);
                    s.add(temp.left.val);
                }
                if(temp.right!=null)
                {
                    q.offer(temp.right);
                    s.add(temp.right.val);
                }
            }
            if(s.contains(x) && s.contains(y))
                return true;
        }
        return false;
    }
}
