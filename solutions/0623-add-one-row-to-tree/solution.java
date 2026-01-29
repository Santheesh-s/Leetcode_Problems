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
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        Queue<TreeNode>q=new LinkedList<>();
        if (depth == 1) {
            TreeNode n = new TreeNode(val);
            n.left = root;
            return n;
        }
        q.offer(root);
        --depth;
        while(!q.isEmpty())
        {
            int size=q.size();
            while (size-- > 0) {
                TreeNode temp = q.poll();

                if (depth == 1) {

                    TreeNode l = new TreeNode(val);
                    TreeNode r = new TreeNode(val);

                    l.left = temp.left;
                    r.right = temp.right;

                    temp.left = l;
                    temp.right = r;

                } else {
                    if (temp.left != null) q.offer(temp.left);
                    if (temp.right != null) q.offer(temp.right);
                }
            }
            if(depth==1) break;
            depth--;
        }
        return root;
    }
}
