struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {

    int len = 0;
    struct ListNode *temp = head;
    while (temp != NULL) {
        len++;
        temp = temp->next;
    }

    if (n > len) {
        return head; 
    }

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

