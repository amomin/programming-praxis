package reluctantsearch;

import static org.junit.Assert.*;

import org.junit.Test;

public class ReluctantSearchTest {

	@Test
	public void testEmpty() {
		int[] arr = {};
		int k = ReluctantSearch.research(arr, 1);
		assertEquals(k, -1);
	}
	
	@Test
	public void testOneElementMiss() {
		int[] arr = {5};
		int k = ReluctantSearch.research(arr, 4);
		assertEquals(k, -1);
	}
	
	@Test
	public void testOneElementHit() {
		int[] arr = {5};
		int k = ReluctantSearch.research(arr, 5);
		assertEquals(k, 0);
	}
	
	@Test
	public void testSeveralElements() {
		int[] arr = {1,3,7,8,22,22,34,45,67,123,234};
		int x;
		x = 1;
		assertEquals(ReluctantSearch.research(arr, x),0);
		x = 5;
		assertEquals(ReluctantSearch.research(arr, x),-1);
		x = 9;
		assertEquals(ReluctantSearch.research(arr, x),-1);
		x = 22;
		// Ambiguous, could return 4 or 5
		//assertEquals(ReluctantSearch.research(arr, x),4);
		//assertEquals(ReluctantSearch.research(arr, x),4);
		x = 122;
		assertEquals(ReluctantSearch.research(arr, x),-1);
		x = 123;
		assertEquals(ReluctantSearch.research(arr, x),9);
		x = 234;
		assertEquals(ReluctantSearch.research(arr, x),10);
		x = 255;
		assertEquals(ReluctantSearch.research(arr, x),-1);
	}
}
