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
    ListNode* partition(ListNode* head, int x) {
        if (!head) return head;

        ListNode* newhead = nullptr;
        ListNode* tail = nullptr;   
        ListNode* temp = head;       
        ListNode* prev = nullptr;    
        ListNode* next = nullptr;  

        while (temp) {
            next = temp->next; 
            if (temp->val < x) 
            {
                if (prev == nullptr) 
                    head = next;
                else 
                    prev->next = next;
                temp->next = nullptr;
                if (!newhead) 
                {
                    newhead = temp;
                    tail = temp;
                } 
                else 
                {
                    tail->next = temp;
                    tail = temp;
                }
            } 
            else
                prev = temp;
            temp = next;
        }

        if (!newhead) return head;
        tail->next = head;
        return newhead;
    }
};

