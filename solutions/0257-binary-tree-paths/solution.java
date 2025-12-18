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
    List<String>ls;
    public Solution()
    {
        this.ls=new ArrayList<>();
    }
    public void preorder(TreeNode root,String a)
    {
        if(root==null)
            return ;
        a+="->"+String.valueOf(root.val);
        if( root.right==null  && root.left==null)
        {
            ls.add(a);
            return ;
        }
        preorder(root.left,a);
        preorder(root.right,a);
    }
    public List<String> binaryTreePaths(TreeNode root) {
        String a="";
        if(root==null)
            return ls;
        a+=String.valueOf(root.val);
        if(root.left==null && root.right==null)
        {
            ls.add(a);
            return ls;
        }
        if(root.left!=null)
            preorder(root.left,a);
        if(root.right!=null)
            preorder(root.right,a);
        return ls;
        
    }
}
