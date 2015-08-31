package slowsort;

import static org.junit.Assert.*;

import org.junit.Test;

/** Just some simple tests, not rigorous */
public class TestSlowsort {

	@Test
	public void testSlowsort() {
		int[] arr = {2, 1, 3};
		assertArrayEquals(Slowsort.slowsort(arr), 
			new int[] {1, 2, 3});
		arr = new int[] {2, 1};
		assertArrayEquals(Slowsort.slowsort(arr), 
			new int[] {1, 2});
		arr = new int[] {1101, 1, 101, 7, 23, 11};
		assertArrayEquals(Slowsort.slowsort(arr), 
			new int[] {1, 7, 11, 23, 101, 1101});
	}
	
	@Test
	public void testFront() {
		int[] arr = {2, 1, 3};
		int[] front = Slowsort.front(arr);
		assertArrayEquals(front, new int[] {2});
		arr = new int[] {1, 3};
		front = Slowsort.front(arr);
		assertArrayEquals(new int[] {1}, front);
		arr = new int[] {3};
		front = Slowsort.front(arr);
		assertArrayEquals(new int[] {}, front);
	}

	@Test
	public void testBack() {
		int[] arr = {2, 1, 3};
		int[] back = Slowsort.back(arr);
		assertArrayEquals(back, new int[] {1, 3});
		arr = new int[] {2, 1};
		back = Slowsort.back(arr);
		assertArrayEquals(back, new int[] {1});
		arr = new int[] {7};
		back = Slowsort.back(arr);
		assertArrayEquals(back, new int[] {7});
	}
	
	@Test
	public void testMerge() {
		int[] front = new int[] {2,5,32};
		int[] back = new int[] {6,4,3};
		assertArrayEquals(new int[] {2,5,32,6,4,3}, Slowsort.merge(front, back));
	}
	
	@Test
	public void testRemoveFirstOccurrance() {
		int[] arr = new int[] {2,5,32,3,5,1,2,4,1};
		int val = 5;
		assertArrayEquals(new int[] {2,32,3,5,1,2,4,1}, 
				Slowsort.removeFirstOccurrance(arr, val));
	}
}