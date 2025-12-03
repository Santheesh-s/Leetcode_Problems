class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ls = new ArrayList<>();
        Stack<TreeNode> stk = new Stack<>();
        TreeNode temp = root;
        if (root == null) return ls;
        while (temp != null || !stk.isEmpty()) {
            while (temp != null) {
                stk.push(temp);
                temp = temp.left;
            }
            temp = stk.pop();
            ls.add(temp.val);
            temp = temp.right;
        }
        return ls;
    }
}

