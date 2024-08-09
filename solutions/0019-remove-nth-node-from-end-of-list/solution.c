struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // Calculate the length of the list
    int len = 0;
    struct ListNode *temp = head;
    while (temp != NULL) {
        len++;
        temp = temp->next;
    }

    // Check if n is greater than the length of the list
    if (n > len) {
        return head; // n is invalid, return the original list
    }

    // Special case: Remove the head node
    if (n == len) {
        struct ListNode* newHead = head->next;
        free(head);
        return newHead;
    }

    // Find the node before the one we want to remove
    int targetIndex = len - n;
    temp = head;
    for (int i = 1; i < targetIndex; i++) {
        temp = temp->next;
    }

    // Remove the nth node from the end
    struct ListNode* nodeToRemove = temp->next;
    temp->next = nodeToRemove->next;
    free(nodeToRemove);

    return head;
}

