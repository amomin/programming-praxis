package identifyingPalindromes;

import static org.junit.Assert.*;

import java.util.LinkedList;

import org.junit.Test;

public class IdentifyingPalindromesTest {

	@Test
	public void testIsPalindromeLinkedListOfInteger() {
		LinkedList<Integer> l = new LinkedList<Integer>();
		l.add(1);
		assert(IdentifyingPalindromes.isPalindrome(l));
		l.add(2);
		assert(!IdentifyingPalindromes.isPalindrome(l));
		l.add(1);
		assert(IdentifyingPalindromes.isPalindrome(l));
		l.removeFirst();
		l.add(2);
		assert(!IdentifyingPalindromes.isPalindrome(l));
		l.add(1);
		assert(IdentifyingPalindromes.isPalindrome(l));
	}

	@Test
	public void testIsPalindromeIntArray() {
		int[] x1 = {1,1};
		assert(IdentifyingPalindromes.isPalindrome(x1));
		int[] x2 = {1,2};
		assert(!IdentifyingPalindromes.isPalindrome(x2));
		int[] x3 = {1,2,1};
		assert(IdentifyingPalindromes.isPalindrome(x3));
		int[] x4 = {1,2,2,1};
		assert(IdentifyingPalindromes.isPalindrome(x4));
	}
}
