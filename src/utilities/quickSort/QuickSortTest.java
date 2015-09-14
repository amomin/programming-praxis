package utilities.quickSort;

import java.util.Arrays;

import utilities.Random;
import static org.junit.Assert.*;

import org.junit.Test;

public class QuickSortTest {

	@Test
	public void test2() {
		int[] tst = new int[]{ 1,2 };
		QuickSort q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, tst[0]);
		assertEquals(2, tst[1]);
		tst = new int[]{ 2,1 };
		q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, tst[0]);
		assertEquals(2, tst[1]);
		tst = new int[]{ 1,1 };
		q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, tst[0]);
		assertEquals(1, tst[1]);
	}
	
	@Test
	public void test3() {
		int[] tst = new int[]{ 1,2,3 };
		QuickSort q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, tst[0]);
		assertEquals(2, tst[1]);
		assertEquals(3, tst[2]);
		tst = new int[]{ 1,3,2 };
		q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, tst[0]);
		assertEquals(2, tst[1]);
		assertEquals(3, tst[2]);
		tst = new int[]{ 3,2,1 };
		q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, tst[0]);
		assertEquals(2, tst[1]);
		assertEquals(3, tst[2]);
		tst = new int[]{ 3,1,2 };
		q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, tst[0]);
		assertEquals(2, tst[1]);
		assertEquals(3, tst[2]);
		tst = new int[]{ 2,3,1 };
		q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, tst[0]);
		assertEquals(2, tst[1]);
		assertEquals(3, tst[2]);
		tst = new int[]{ 2,1,3 };
		q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, tst[0]);
		assertEquals(2, tst[1]);
		assertEquals(3, tst[2]);
	}
	
	@Test
	public void testQuickSortRandomArrays() {
		for (int i = 0; i < 10; i++) {
			int[] tst = Random.intArray(5, 10);
			int[] cpy = Arrays.copyOf(tst, tst.length);
			QuickSort q = new QuickSort(tst);
			tst = q.sort();
			Arrays.sort(cpy);
			assertArrayEquals(cpy, tst);
		}
	}

	@Test
	public void testQuickFindSize2() {
		int[] tst = new int[]{ 1,2 };
		QuickSort q = new QuickSort(tst);
		assertEquals(1, q.find(1));
		assertEquals(2, q.find(2));
		tst = new int[]{ 2,1 };
		q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, q.find(1));
		assertEquals(2, q.find(2));
		tst = new int[]{ 1,1 };
		q = new QuickSort(tst);
		tst = q.sort();
		assertEquals(1, q.find(1));
		assertEquals(1, q.find(2));
	}

	/** Tests all possible permutations of finding the 
	 * kth element of a permutation of {1,2,3} for
	 * k = 1,2,3 (in some order).
	 */
	@Test
	public void testQuickFind3Elements() {
		int[][] permutations = new int[][] {
				{1,2,3},
				{1,3,2},
				{2,1,3},
				{2,3,1},
				{3,1,2},
				{3,2,1}
		};
		for (int i = 0; i < 6; i++) {
			int[] p = Arrays.copyOf(permutations[i],3);
			for (int j = 0; j < 6; j++) {
				int[] order = Arrays.copyOf(permutations[j],3);
				QuickSort q = new QuickSort(p);
				assertEquals(order[0], q.find(order[0]));
				assertEquals(order[1], q.find(order[1]));
				assertEquals(order[2], q.find(order[2]));
			}
		}
	}
	
	/** Tests all possible permutations of finding the 
	 * kth element of a permutation of {1,2,2} for
	 * k = 1,2,3 (in some order).
	 */
	@Test
	public void testQuickFind3ElementsWithRepeats() {
		int[] sorted = new int[] {1,2,2};
		int[][] tests = new int[][] {
				{1,2,2},
				{2,1,2},
				{2,2,1}
		};
		int[][] permutations = new int[][] {
				{1,2,3},
				{1,3,2},
				{2,1,3},
				{2,3,1},
				{3,1,2},
				{3,2,1}
		};
		for (int i = 0; i < 3; i++) {
			int[] test = Arrays.copyOf(tests[i],3);
			for (int j = 0; j < 6; j++) {
				int[] order = Arrays.copyOf(permutations[j],3);
				QuickSort q = new QuickSort(test);
				assertEquals(sorted[order[0]-1], q.find(order[0]));
				assertEquals(sorted[order[1]-1], q.find(order[1]));
				assertEquals(sorted[order[2]-1], q.find(order[2]));
			}
		}
	}
	
	@Test
	public void testQuickFindRandom() {
		int SIZE = 100;
		int MAX = 1000;
		for (int i = 0; i < 10; i++) {
			int[] tst = new int[SIZE];
			for(int x = 0; x < SIZE; x++) {
				tst[x] = Random.integer(MAX);
			}
			int[] cpy = Arrays.copyOf(tst, SIZE);
			int k = Random.integer(1,SIZE);
			QuickSort q = new QuickSort(tst);
			int actual = q.find(k);
			Arrays.sort(cpy);
			int expected = cpy[k-1];
			assertEquals(expected,actual);
		}
	}
}
