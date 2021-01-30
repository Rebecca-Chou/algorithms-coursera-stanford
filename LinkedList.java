class LinkedList {
	
	static class Node {
		int value;
		Node next;
	
		public Node(int value) {
			this.value = value;
		}
	}

	Node first = null;

	public void addAtFront(Node node) {
		node.next = first;
		first = node;
	}
	
	public void addAtEnd(Node node) {
		if (first == null)
			first = node;
		else {
            Node p = first;
            while(p.next!=null)
                p = p.next;
            p.next = node;
		}
	}
	
	public void removeFront() {
		first = first.next;
	}

	public void print() {
		Node p = first;
		while(p != null) {
			System.out.print(p.value+" -> ");
			p = p.next;
        }
	}

	public static void main(String[] args) {
		LinkedList L = new LinkedList();
		L.addAtFront(new Node(1));
		L.addAtFront(new Node(2));
		L.addAtFront(new Node(4));
		L.addAtFront(new Node(8));
		L.addAtEnd(new Node(5));
        L.print();
        L.print();
	}
}