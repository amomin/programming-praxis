package identifyingPalindromes;

import java.util.LinkedList;
import java.util.Stack;

/** We will ignore that a LinkedList is
 * doubly linked in the java implementation.
 * 
 * Ah, we cheated in using the length of the list. 
 * Praxis points out that you can use the
 * "tortoise-hare" method to deal with this case
 * (have two pointers, advancing "the hare" twice for every 
 * advance of "the tortoise").
 * @author amomin
 */
public class IdentifyingPalindromes {

	public static boolean isPalindrome(LinkedList<Integer> x) {
		Stack<Integer> s = new Stack<Integer>();
	
		int i = 0;
		int n = x.size();
		while (i < n/2) {
			Integer l = x.remove();
			s.push(l);
			i++;
		}
		if (n % 2 == 1) {
			x.remove();
		}
		while (!x.isEmpty() && !s.isEmpty()) {
			Integer l = x.remove();
			Integer r = s.pop();
			if (l != r) {
				return false;
			}
		}
		return true;
	}
	public static boolean isPalindrome(int[] x) {
		int n = x.length;
		for (int i = 0; i < n/2; i++) {
			if (x[i] != x[n - 1 - i]) {
				return false;
			}
		}
		return true;
	}
}
