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
    ListNode *reverse(ListNode *head)
    {
        ListNode *prev=NULL,*cur=head,*next=NULL;
        while(cur)
        {
            next=cur->next;
            cur->next=prev;
            prev=cur;
            cur=next;
        }
        return prev;
    }
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        ListNode *start=head,*prev=NULL,*cur=head,*temp,*rev;
        int count=1,i;
        while(cur)
        {
            for(i=1;i<count && cur;i++,cur=cur->next);
            if(cur==NULL)i--;
            if(i%2==0)
            {
                if(cur==NULL)temp=NULL;
                else 
                {   
                    temp=cur->next;
                    cur->next=NULL;
                }
                rev=reverse(start);
                if(prev) prev->next=rev;
                else head=rev;
                prev=start;
                cur=start=temp;
            }
            else
            {
                if(prev)
                prev->next=start;
                prev=cur;
                if(cur)
                cur=cur->next;
                start=cur;
            }
            count++;
        }
        return head;
    }
};
