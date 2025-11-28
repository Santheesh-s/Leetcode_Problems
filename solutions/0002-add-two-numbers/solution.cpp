class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;

        ListNode *head1 = l1, *head2 = l2;
        ListNode *prev1 = nullptr, *prev2 = nullptr;
        int carry = 0;
        while (l1 && l2) {
            int sum = l1->val + l2->val + carry;
            carry = sum / 10;
            int digit = sum % 10;
            l1->val = digit;
            l2->val = digit;

            prev1 = l1;
            prev2 = l2;

            l1 = l1->next;
            l2 = l2->next;
        }
        if (l1) {
            while (l1) {
                int sum = l1->val + carry;
                carry = sum / 10;
                l1->val = sum % 10;
                prev1 = l1;
                l1 = l1->next;
            }
            if (carry) prev1->next = new ListNode(carry);
            return head1;
        }
        if (l2) {
            while (l2) {
                int sum = l2->val + carry;
                carry = sum / 10;
                l2->val = sum % 10;
                prev2 = l2;
                l2 = l2->next;
            }
            if (carry) prev2->next = new ListNode(carry);
            return head2;
        }
        if (carry) {
            prev1->next = new ListNode(carry);
        }
        return head1;
    }
};

