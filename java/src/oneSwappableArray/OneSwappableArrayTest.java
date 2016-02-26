package oneSwappableArray;

import static org.junit.Assert.*;

import org.junit.Test;

public class OneSwappableArrayTest {

	@Test
	public void testisOneSwapFromSorted() {
		//fail("Not yet implemented");
		int [] arr = new int[] {1};
		assertFalse(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {1,2};
		assertFalse(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {2 ,1};
		assertTrue(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {22,11};
		assertTrue(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {2 ,1, 3};
		assertTrue(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {1, 3 ,2, 4};
		assertTrue(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {4, 2 ,3, 1};
		assertTrue(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {4, 3 ,2, 1};
		assertFalse(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {30, 20, 10, 40};
		assertTrue(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {40, 20 ,10, 30};
		assertFalse(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {1,5,3,4,2};
		assertTrue(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {5,2,3,4,1};
		assertTrue(OneSwappableArray.isOneSwapFromSorted(arr));
		arr = new int[] {5,2,4,3,1};
		assertFalse(OneSwappableArray.isOneSwapFromSorted(arr));
	}

	@Test
	public void testisOneSwapFromSortedTrueCase() {
		for (int cnt = 0; cnt < 1000; cnt++) {
			int[] arr = {1,2,3,4,5,6,7,8,9,10};
			swapOne(arr);
			assertTrue(OneSwappableArray.isOneSwapFromSorted(arr));
		}
	}
	
	@Test
	public void testTwoSwapsFromSortedReturnsFalse() {
		for (int cnt = 0; cnt < 1000; cnt++) {
			int[] arr1 = {1,2,3,4,5};
			swapOne(arr1);
			int[] arr2 = {6,7,8,9,10};
			swapOne(arr2);
			int[] arr = intArrconcat(arr1, arr2);
			assertFalse(OneSwappableArray.isOneSwapFromSorted(arr));
		}
	}
	
	private void swapOne(int[] arr) {
		int n = arr.length;
		int i = (int) (Math.random() * n - 1);
		int j = i + 1 + (int) Math.floor((Math.random() * (n - i - 1)));
		int temp = arr[j];
		arr[j] = arr[i];
		arr[i] = temp;
	}
	
	private int[] intArrconcat(int[] a, int[] b) {
		   int aLen = a.length;
		   int bLen = b.length;
		   int[] c= new int[aLen+bLen];
		   System.arraycopy(a, 0, c, 0, aLen);
		   System.arraycopy(b, 0, c, aLen, bLen);
		   return c;
		}
}