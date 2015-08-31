package kthLargestItem;

import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;

public class KthLargestItemTest {

	@Test
	public void testFindEdgeCases() {
		int[] arrl1 = {};
		IIntegerList l = new IntegerList(arrl1);
		assertEquals(null, KthLargestItem.find(l, 2));
		int[] arrl2 = {1};
		l = new IntegerList(arrl2);
		assertEquals(new Integer(1), KthLargestItem.find(l, 1));
		assertEquals(null, KthLargestItem.find(l, 2));
	}
	
	@Test
	public void testFind() {
		int[] arrl = {5,2,4,1,8,5,6};
		IIntegerList l = new IntegerList(arrl);
		
		assertEquals(new Integer(2), KthLargestItem.find(l, 2));
		assertEquals(null, KthLargestItem.find(l, 22));
		assertEquals(new Integer(4), KthLargestItem.find(l, 3));
		assertEquals(new Integer(4), KthLargestItem.find(l, 3));
	}

	@Test
	public void testFindRandom() {
		for (int j = 0; j < 10; j++) {
			int N = (int) Math.floor(Math.random() * 1000);
			int k = 1 + (int) Math.floor(0.1 * Math.random() * N);
			int[] arrl = new int[N];
			for (int i = 0; i < N; i++) {
				arrl[i] = (int) Math.floor(Math.random() * N);
			}
			int[] arrcopy = Arrays.copyOf(arrl, N);
			Arrays.sort(arrcopy);
			Integer answer = arrcopy[k-1];
			IIntegerList l = new IntegerList(arrl);
			assertEquals(answer, KthLargestItem.find(l, k));
		}
	}
}
