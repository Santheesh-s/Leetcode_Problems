/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB) return NULL;
        ListNode *temp=headA;
        while(temp->next!=NULL)
            temp=temp->next;
        temp->next=headB;
        ListNode *slow=headA,*fast=headA;
        bool cycle = false;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                cycle = true;
                break;
            }
        }
        if (!cycle) {
            temp->next = NULL;
            return NULL;
        }
        
        slow=headA;
        while(fast!=slow )
        {
            fast=fast->next;
            slow=slow->next;
        }
        temp->next=NULL;
        return slow;
    }
};
