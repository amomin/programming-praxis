package PatienceSorting;

import java.util.*;


public class PatienceSorting {

	public static int[] sort(int[] list, boolean debug) {

		Node n = new Node();
		for (Integer i : list) {
			n.enqueue(i);
		}

		int length = list.length;
		int[] result = new int[length];
		
		int count = 0;

		Node currentLeast;
		Node current;
		Integer least;
		while (count < length) {
			result[count] = n.dequeue();
			if (debug) {
				System.out.println(n.asString());
				System.out.println(result[count]);
			}
			count ++;	
		}
		
		return result;
	}

	private static class Node {
		Stack<Integer> s;
		private Node next;
		private Node prev;

		public Node() {
			s = new Stack<Integer>();
			next = null;
		}

		public void enqueue(int x) {
			if (!s.empty()) {
				int y = s.peek();
				if (x < y)
						s.push(x);
				else {
					if (next != null) {
						next.enqueue(x);
					} else {
						next = new Node();
						next.prev = this;
						next.enqueue(x);
					}
				}
			} else {
				s.push(x);
			}
		}


		public int peekLeast() {
			int thisLeast = s.peek();
			if (next != null) {
				int nextLeast = next.peekLeast();
				if (thisLeast < nextLeast) {
					return thisLeast;
				} else {
					return nextLeast;
				}
			} else {
				return thisLeast;
			}
		}

		public int dequeue() {
			int result;
			int thisLeast = s.peek();
			if (next != null) {
				int nextLeast = next.peekLeast();
				if (thisLeast < nextLeast) {
					result = s.pop();
					if (s.empty()) { 
						// Unlink
						if (prev != null) {
							prev.next = next;
							if (next != null) next.prev = prev;
						}
						else { // First item in list must be preserved, replace with next
							if (next != null) {
								s = next.s;
								if (next.next != null) next.next.prev = this;
								next = next.next;
							}
						}
					}
				} else {
					result = next.dequeue();
				}
				return result;
			} else { // next == null
				result = s.pop();
				if (s.empty()) { // Remove from (end of) list
					if (prev != null) {
						prev.next = null;
						prev = null;
					}
				}
			}
			return result;
		}

		/** String representation for debugging purposes
		 *
		 */
		public String asString() {
			Node current = this;
			String output = new String(); output = "";
			while (current != null) {
				for (Integer i : current.s) {
					output += String.valueOf(i) + ",";
				}
				output += " ";
				current = current.next;
			}
			return output;
		}
	}

}
