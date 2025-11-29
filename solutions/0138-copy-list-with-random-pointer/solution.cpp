/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    void dup(Node* head,Node* next,Node* rand)
    {
        head->next=new Node(head->val);
        head->next->next=next;
        head->next->random=rand;
    }
    Node* copyRandomList(Node* head) {
        if (!head) return NULL;
        Node *temp=head;
        while(temp)
        {
            dup(temp,temp->next,temp->random);
            temp=temp->next->next;
        }
        temp=head;
        while(temp)
        {
            if(!temp->random)
                temp->next->random=NULL;
            else
                temp->next->random=temp->random->next;
            temp=temp->next->next;
        }Node* orig = head;
        Node* copyHead = head->next;
        Node* copy = copyHead;

        while (orig) {
            orig->next = copy->next;
            orig = orig->next;              

            if (orig) {
                copy->next = orig->next;    
                copy = copy->next;   
            } else {
                copy->next = nullptr;
            }
        }
        return copyHead;
    }
};
