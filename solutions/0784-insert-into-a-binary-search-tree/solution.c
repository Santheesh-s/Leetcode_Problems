/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {
    struct TreeNode *temp,*newnode=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    newnode->val=val;
    newnode->left=NULL;
    newnode->right=NULL;
    if(root==NULL)
        root=newnode;
    else
    {
        temp=root;
        while(1)
        {
            if(val<temp->val)
            {
                if(temp->left==NULL)
                {
                    temp->left=newnode;
                    break;
                }
                else
                    temp=temp->left;
            }
            if(val>temp->val)
            {
                if(temp->right==NULL)
                {
                    temp->right=newnode;
                    break;
                }
                else
                    temp=temp->right;
            }
        }
    }
    return root;
}
