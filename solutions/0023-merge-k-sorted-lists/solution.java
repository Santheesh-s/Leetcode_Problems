
class Solution{
    public ListNode mergeKLists(ListNode[] lists) {
        List<Integer> list = new ArrayList<>();

        // Traverse each linked list and add values to the list
        for (ListNode node : lists) {
            while (node != null) {
                list.add(node.val);
                node = node.next;
            }
        }

        // Sort the list
        Collections.sort(list);

        // Create a new sorted linked list from the sorted list of values
        ListNode dummy = new ListNode(0); // Dummy node to simplify list creation
        ListNode current = dummy;
        for (int val : list) {
            current.next = new ListNode(val);
            current = current.next;
        }

        // Return the merged and sorted linked list
        return dummy.next;
    }
}

