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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        Queue<TreeNode>q=new LinkedList<>();
        List<List<Integer>>ls=new ArrayList<>();
        if(root==null)
            return ls;
        q.offer(root);
        while(!q.isEmpty())
        {
            int size=q.size();
            List<Integer>ls1=new ArrayList<>();
            while(size-->0)
            {
                TreeNode temp=q.poll();
                ls1.add(temp.val);
                if(temp.left!=null)
                    q.offer(temp.left);
                if(temp.right!=null)
                    q.offer(temp.right);
            }
            ls.add(ls1);
        }
        Collections.reverse(ls);
        return ls;
    }
}
