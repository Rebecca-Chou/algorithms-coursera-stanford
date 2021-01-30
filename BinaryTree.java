import java.util.Random;
public class BinaryTree {
 
	class Node {
		int data;
		Node left, right;
 
		public Node(int item) {
			data = item;
			left = right = null;
		}
	}

	Node root;
 
	BinaryTree() { 
		root = null; 
	}
 
	void insert(int data) {
	   root = recInsert(root, data);
	}
	 
	Node recInsert(Node root, int data) {
		Random rn = new Random();
		int rand = rn.nextInt() % 2;
		if (root == null) {
			root = new Node(data);
			return root;
		}
		if (rand == 0)
			root.left = recInsert(root.left, data);
		else
			root.right = recInsert(root.right, data);

		return root;
	}

	void print(Node root, int space, int t) {
	  int COUNT = 3;

	  if(root == null)
		return;

	  space += COUNT;

	  print(root.right, space, 1);

	  for(int i = COUNT; i < space; i++) {
		System.out.print(" ");
	  }
	  if(t == 1) {
		System.out.println("/ " + root.data);
	  }
	  else if (t == 2) {
		System.out.println("\\ " + root.data);
	  }else{
		  System.out.println(root.data);
	   }

	   print(root.left, space, 2);
	 }

	public static void main(String[] args) {
	  BinaryTree t = new BinaryTree();

	  t.insert(5);
	  t.insert(3);
	  t.insert(8);
	  t.insert(1);
	  t.insert(4);
	  t.insert(7);
	  t.insert(9);
	  t.insert(0);
	  t.insert(2);
	  t.insert(6);
	  t.insert(10);

	  t.print(t.root, 0, 0);
	}
}