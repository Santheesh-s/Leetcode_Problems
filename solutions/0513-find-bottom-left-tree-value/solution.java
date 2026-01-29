class Solution {
    public int findBottomLeftValue(TreeNode root) {
        if(root.left==null && root.right==null) return root.val;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int ans=root.val;
        while (!q.isEmpty()) {
            int size = q.size();
            ans = q.peek().val;   
            while (size-- > 0) {
                TreeNode node = q.poll();
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
        }
        return ans;
    }
}

