/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int sum1=0;
void preorder(struct TreeNode *root,int sum)
{
    if (root == NULL)
        return;
    sum = sum * 10 + root->val;
    if(root->left==NULL && root->right==NULL)
    {
        sum1+=sum;
        return;
    }
    preorder(root->left,sum);
    preorder(root->right,sum);
}
int sumNumbers(struct TreeNode* root) 
{
    sum1 = 0;
    preorder(root,0);
    return sum1;
}
