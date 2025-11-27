// /**
//  * Definition for singly-linked list.
//  * struct ListNode {
//  * int val;
//  * ListNode *next;
//  * ListNode() : val(0), next(nullptr) {}
//  * ListNode(int x) : val(x), next(nullptr) {}
//  * ListNode(int x, ListNode *next) : val(x), next(next) {}
//  * };
//  */
// class Solution {
// public:
//     ListNode* reverseBetween(ListNode* head, int left, int right) {
//         if(!head || !head->next) return head;
        
//         ListNode *prev=NULL, *temp=NULL, *cur=head;
//         int a=0;

//         while(++a!=left)
//         {
//             prev=cur;
//             cur=cur->next;
//         }

//         ListNode *con = prev; 
//         ListNode *tail = cur; 
        
//         prev = NULL; 

//         while(left <= right--) 
//         {
//             temp=cur->next;
//             cur->next=prev;
//             prev=cur;
//             cur=temp;
//         }
//         if(con != NULL) {
//             con->next = prev;
//         } else {
//             head = prev; 
//         }
        
//         tail->next = cur; 
//         return head;
//     }
// };

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

    ListNode* reverseBetween(ListNode* head, int left, int right) {

        if(!head || !head->next) return head;

        ListNode *prev=NULL,*temp=NULL,*cur=head;

        int a=0;

        while(++a!=left)
        {
            prev=cur;
            cur=cur->next;
        }
        ListNode *tail=cur,*con=prev;prev=NULL;
        while(left<=right--)
        {
            temp=cur->next;
            cur->next=prev;
            prev=cur;
            cur=temp;
        }
        if(con != NULL)
            con->next = prev;
        else 
            head = prev;
        tail->next = cur;
        return head;
    }

};
