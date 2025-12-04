/**
 * Definition for a binary tree node->
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(NULLptr), right(NULLptr) {}
 *     TreeNode(int x) : val(x), left(NULLptr), right(NULLptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        return finder(root,targetSum,0);
    }
    bool finder(TreeNode* root,int targetSum,int sum)
    {
        if(root==NULL)
            return false;
        sum+=root->val;
        if(root->left==NULL && root->right==NULL)
            return targetSum==sum;
        return finder(root->left,targetSum,sum) || finder(root->right,targetSum,sum);
    }
};
