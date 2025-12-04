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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>>ls=new ArrayList<>();
        Queue<TreeNode>q=new LinkedList<>();
        if(root==null) return ls;
        q.offer(root);
        int size=1;
        while(!q.isEmpty())
        {
            size=q.size();
            List<Integer>ls1=new ArrayList<>();
            while(size>0)
            {
                TreeNode temp=q.poll();
                ls1.add(temp.val);
                if(temp.left!=null)
                    q.offer(temp.left);
                if(temp.right!=null)
                    q.offer(temp.right);
                size-=1;
            }
            ls.add(ls1);
        }
        return ls;
    }
}
