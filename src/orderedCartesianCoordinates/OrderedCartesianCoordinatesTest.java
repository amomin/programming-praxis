package orderedCartesianCoordinates;

import static org.junit.Assert.*;

import org.junit.Test;

public class OrderedCartesianCoordinatesTest {

	final static int NUMTESTS = 1000;
	
	@Test
	public void benchMarkSolution1() {
		OrderedCartesianCoordinates.solution1(NUMTESTS);
	}

	/*
	@Test
	public void benchMarkSolution2() {
		OrderedCartesianCoordinates.solution2(NUMTESTS);
	}
	*/
	
	@Test
	public void benchMarkSolution3() {
		OrderedCartesianCoordinates.solution3(NUMTESTS);
	}
	
	@Test
	public void testSolution1() {
		fail("Not yet implemented");
	}

}
