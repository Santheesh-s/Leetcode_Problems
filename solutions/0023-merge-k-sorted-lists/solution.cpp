/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* merge(ListNode* head1,ListNode* head2)
    {
        ListNode *temp1=head1,*temp2=head2,*head=new ListNode(0);
        ListNode* dummy=head;
        while(temp1 && temp2)
        {
            if(temp1->val<temp2->val)
            {
                head->next=temp1;
                head=head->next;
                temp1=temp1->next;
            }
            else
            {
                head->next=temp2;
                head=head->next;
                temp2=temp2->next;
            }
        }
        while(temp1)
        {
            head->next=temp1;
            head=head->next;
            temp1=temp1->next;
        }
        while(temp2)
        {
            head->next=temp2;
            head=head->next;
            temp2=temp2->next;
        }
        return dummy->next;
    }
    ListNode* mergeKLists(vector<ListNode*>& lists) 
    {
        int n=lists.size();
        if(n==0)return NULL;
        while(n>1)
        {
            int index=0;
            for(int i=0;i<n;i+=2)
            {
                if(i+1<n)
                    lists[index++]=merge(lists[i],lists[i+1]);
                else
                    lists[index++]=lists[i];
                
            }
            n=index;
        }
        return lists[0];
    }
};
