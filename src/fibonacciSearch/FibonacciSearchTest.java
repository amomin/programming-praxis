package fibonacciSearch;

import static org.junit.Assert.*;

import org.junit.Test;

public class FibonacciSearchTest {

	@Test
	public void testFibSearch() {
		assertEquals(-1, FibonacciSearch.fibSearch((new int[] {}), 1));
		assertEquals(0,  FibonacciSearch.fibSearch((new int[] {1}), 1));
		assertEquals(-1,  FibonacciSearch.fibSearch((new int[] {1}), 2));
		assertEquals(-1, FibonacciSearch.fibSearch((new int[] {5,7}), 6));
		assertEquals(0,  FibonacciSearch.fibSearch((new int[] {5,7}), 5));
		assertEquals(-1, FibonacciSearch.fibSearch((new int[] {5,7}), 7));
		assertEquals(2,  FibonacciSearch.fibSearch((new int[] {5,7,234}), 7));
		assertEquals(2,  FibonacciSearch.fibSearch((new int[] {5,7,234,1987}), 7),2);
		assertEquals(1,  FibonacciSearch.fibSearch((new int[] {1,2,3,4,5,7,234,1987}), 1));
		assertEquals(2,  FibonacciSearch.fibSearch((new int[] {1,2,3,4,5,7,234,1987}), 2));
		assertEquals(5,  FibonacciSearch.fibSearch((new int[] {1,2,3,4,5,7,234,1987}), 7));
		assertEquals(7,  FibonacciSearch.fibSearch((new int[] {1,2,3,4,5,7,234,1987}), 1987));
		/*
		*/
	}
	
	@Test
	public void testIndexFloor() {
		assertEquals(2, FibonacciSearch.indexFloor(1));
		assertEquals(3, FibonacciSearch.indexFloor(2));
		for (int i = 4; i < 15; i++) {
			int fib = FibonacciSearch.fibonacci(i);
			assertEquals(i - 1, FibonacciSearch.indexFloor(fib - 1));
			assertEquals(i, FibonacciSearch.indexFloor(fib));
			assertEquals(i, FibonacciSearch.indexFloor(fib + 1));
		}
	}
	
	@Test
	public void testIndexCeil() {
		assertEquals(0, FibonacciSearch.indexCeil(0));
		assertEquals(1, FibonacciSearch.indexCeil(1));
		assertEquals(3, FibonacciSearch.indexCeil(2));
		assertEquals(4, FibonacciSearch.indexCeil(3));
		assertEquals(5, FibonacciSearch.indexCeil(4));
		for (int i = 5; i < 15; i++) {
			int fib = FibonacciSearch.fibonacci(i);
			assertEquals(i, FibonacciSearch.indexCeil(fib - 1));
			assertEquals(i, FibonacciSearch.indexCeil(fib));
			assertEquals(i + 1, FibonacciSearch.indexCeil(fib + 1));
		}
	}
}