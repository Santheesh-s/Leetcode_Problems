class Node {
    int val;
    Node next;
    public Node(int val) {
        this.val = val;
        this.next = null;
    }
}

class MyLinkedList {
     Node head;
     Node tail;
     int size;

    public MyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

    public int get(int index) {
        if(index < 0 || index >= size) return -1;
        Node temp = head;
        for(int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp.val;
    }

    public void addAtHead(int val) {
        Node node = new Node(val);
        node.next = head;
        head = node;
        if(tail == null) tail = node;
        size++;
    }

    public void addAtTail(int val) {
        Node node = new Node(val);
        if(tail == null) {
            head = tail = node;
        } else {
            tail.next = node;
            tail = node;
        }
        size++;
    }

    public void addAtIndex(int index, int val) {
        if(index < 0 || index > size) return;
        if(index == 0) {
            addAtHead(val);
            return;
        }
        if(index == size) {
            addAtTail(val);
            return;
        }
        Node temp = head;
        for(int i = 0; i < index - 1; i++) {
            temp = temp.next;
        }
        Node node = new Node(val);
        node.next = temp.next;
        temp.next = node;
        size++;
    }

    public void deleteAtIndex(int index) {
        if(index < 0 || index >= size) return;

        if(index == 0) {
            head = head.next;
            size--;
            if(head == null) tail = null;
            return;
        }

        Node prev = head;
        for(int i = 0; i < index - 1; i++) {
            prev = prev.next;
        }

        if(index == size - 1) {
            tail = prev;
            prev.next = null;
        } else {
            prev.next = prev.next.next;
        }

        size--;
    }
}
