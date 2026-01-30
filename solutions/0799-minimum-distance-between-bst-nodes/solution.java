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
    
    public int minDiffInBST(TreeNode root) {
        int arr[]=new int[101];
        int k=0;
        Queue<TreeNode>q=new LinkedList<>();

        q.offer(root);
        int min=Integer.MAX_VALUE;
        while(!q.isEmpty())
        {
            int size=q.size();
            while(size-->0)
            {
                TreeNode temp=q.poll();
                arr[k++]=temp.val;
                if(temp.left!=null)
                    q.offer(temp.left);
                if(temp.right!=null)
                    q.offer(temp.right);
            }
        }
        Arrays.sort(arr, 0, k);
        for(int i=1;i<k;i++)
            min=Math.min(min,arr[i]-arr[i-1]);
        return min;
    }
}
