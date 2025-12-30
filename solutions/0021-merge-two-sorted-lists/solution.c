/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode *res = &dummy;

    while(list1 && list2)
    {
        if(list1->val>list2->val)
        {
            res->next=list2;
            res=res->next;
            list2=list2->next;
        }
        else
        {
            res->next=list1;
            res=res->next;
            list1=list1->next;
        }
    }
    if(list1)
        res->next=list1;
    else
        res->next=list2;
    return dummy.next;
}
