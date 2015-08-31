package kthLargestItem;

import static org.junit.Assert.*;

import org.junit.Test;

public class MinStackTest {

	@Test
	public void testEdgeCase() {
		MinStack ms = new MinStack(1);
		assertEquals(0, ms.size());
		ms.insert(1);
		assertEquals(new Integer(1), ms.getValue());
	}
	
	@Test
	public void testSize() {
		MinStack ms = new MinStack(3);
		assertEquals(0, ms.size());
		ms.insert(5);
		ms.insert(4);
		assertEquals(2, ms.size());
		ms.insert(3);
		ms.insert(2);
		assertEquals(3, ms.size());
	}

	@Test
	public void testGetValue() {
		MinStack ms = new MinStack(3);
		ms.insert(5);
		ms.insert(4);
		ms.insert(3);
		ms.insert(2);
		assertEquals(new Integer(4), ms.getValue());
	}
}
