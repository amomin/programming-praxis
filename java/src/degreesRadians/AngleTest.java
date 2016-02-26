package degreesRadians;

import static org.junit.Assert.*;

import org.junit.Test;

/** Haven't tested exceptions... oh well.
 * 
 */
public class AngleTest {

	private static final double EPSILON = 0.0001;
	
	@Test
	public void testFromDegrees() {
		Angle a = Angle.fromDegrees(0, 0, 0);
		a = Angle.fromDegrees(360, 0, 0);
		a = Angle.fromDegrees(180, 59, 10);
		a = Angle.fromDegrees(720, 0, 0);
	}

	@Test
	public void testFromRadians() {
		Angle a = Angle.fromRadians(0);
		a = Angle.fromRadians(6*Math.PI);
		a = Angle.fromRadians(Math.PI);
		a = Angle.fromRadians(1);
	}

	@Test
	public void testDegrees() {
		Angle a = Angle.fromDegrees(0, 0, 0);
		assertEquals(0, a.degrees());
		a = Angle.fromDegrees(360, 0, 0);
		assertEquals(0, a.degrees());
		a = Angle.fromDegrees(720, 0, 0);
		assertEquals(0, a.degrees());
		a = Angle.fromDegrees(180, 27, 36);
		assertEquals(180, a.degrees());
		a = Angle.fromDegrees(27, 14, 12);
		assertEquals(27, a.degrees());
		a = Angle.fromDegrees(361, 11, 2);
		assertEquals(1, a.degrees());
		a = Angle.fromDegrees(720, 10, 5);
		assertEquals(0, a.degrees());
	}

	@Test
	public void testMinutes() {
		Angle a = Angle.fromDegrees(0, 0, 0);
		assertEquals(0, a.minutes());
		a = Angle.fromDegrees(360, 0, 0);
		assertEquals(0, a.minutes());
		a = Angle.fromDegrees(720, 0, 0);
		assertEquals(0, a.minutes());
		a = Angle.fromDegrees(180, 27, 36);
		assertEquals(27, a.minutes());
		a = Angle.fromDegrees(27, 14, 12);
		assertEquals(14, a.minutes());
		a = Angle.fromDegrees(361, 11, 2);
		assertEquals(11, a.minutes());
		a = Angle.fromDegrees(720, 10, 5);
		assertEquals(10, a.minutes());
		a = Angle.fromRadians(0.0130899694);
		assertEquals(45, a.minutes());
	}

	@Test
	public void testSeconds() {
		Angle a = Angle.fromDegrees(0, 0, 0);
		assertEquals(0, a.seconds());
		a = Angle.fromDegrees(360, 0, 0);
		assertEquals(0, a.seconds());
		a = Angle.fromDegrees(720, 0, 0);
		assertEquals(0, a.seconds());
		a = Angle.fromDegrees(180, 27, 36);
		assertEquals(36, a.seconds());
		a = Angle.fromDegrees(27, 14, 12);
		assertEquals(12, a.seconds());
		a = Angle.fromDegrees(361, 11, 2);
		assertEquals(2, a.seconds());
		a = Angle.fromDegrees(720, 10, 5);
		assertEquals(5, a.seconds());
		a = Angle.fromRadians(0.000208469883);
		assertEquals(43, a.seconds());
		a = Angle.fromRadians(0.0000581776417);
		assertEquals(12, a.seconds());
	}

	@Test
	public void testRadians() {
		Angle a = Angle.fromDegrees(0, 0, 0);
		assertTrue(Math.abs(a.radians()) < EPSILON);
		a = Angle.fromDegrees(360, 0, 0);
		assertTrue(Math.abs(a.radians()) < EPSILON);
		a = Angle.fromRadians(0.0);
		assertTrue(Math.abs(a.radians()) < EPSILON);
		a = Angle.fromDegrees(90, 0, 0);
		assertTrue(Math.abs(a.radians() - (Math.PI / 2)) < EPSILON);
		a = Angle.fromDegrees(450, 0, 0);
		assertTrue(Math.abs(a.radians() - (Math.PI / 2)) < EPSILON);
		double rads = 5.23243234;
		a = Angle.fromRadians(rads);
		assertTrue(Math.abs(a.radians() - rads) < EPSILON);
		for (int i = 0; i < 10; i++) {
			double d = Math.random();
			a = Angle.fromRadians(d*2*Math.PI
				 + 2*Math.PI * 5*(Math.floor(d * 5))
				);
			assertTrue(Math.abs(a.radians() - d*Math.PI*2) < EPSILON);
		}
	}

}
