/**
 * Definition for a binary tree node->
 * struct TreeNode {
 *     long long val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(long long x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(long long x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    long long MOD=pow(10,9)+7;
    long long maxPro,total;
    long long sum(TreeNode *root)
    {
        if(root==NULL) 
            return 0;
        return root->val+sum(root->left)+sum(root->right);
    }

    long long dfsMax(TreeNode *root)
    {
        if (root==NULL)
            return 0;
        long long left=dfsMax(root->left);
        long long right=dfsMax(root->right);

        long long subtree=root->val+left+right;
        maxPro=max(maxPro , subtree*(total-subtree));
        return subtree;
    }

    long long maxProduct(TreeNode* root) {
        if(root==NULL) return 0;
        maxPro=0;
        total=sum(root);
        dfsMax(root);
        return maxPro%MOD;
    }
};
