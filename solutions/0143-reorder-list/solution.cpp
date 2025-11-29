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
    ListNode* reverse(ListNode *head)
    {
        ListNode *prev = nullptr, *cur = head, *next = nullptr;
        while (cur)
        {
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

    void reorderList(ListNode* head) {
        if (!head || !head->next) return;

        ListNode *slow = head, *fast = head;
        ListNode *prev = nullptr;            
        ListNode *newhead = nullptr, *tail = nullptr;
        while (fast && fast->next)
        {
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        if (prev) prev->next = nullptr;
        ListNode *temp = reverse(slow);
        ListNode *first = head;
        ListNode *second = temp;

        while (first && second)
        {
            ListNode *n1 = first->next;
            ListNode *n2 = second->next;
            first->next = second;
            if (!n1) break;
            second->next = n1;

            first = n1;
            second = n2;
        }
        newhead = head;
        tail = newhead;
        while (tail && tail->next) tail = tail->next;
    }
};

