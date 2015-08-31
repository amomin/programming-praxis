package orderedCartesianCoordinates;

import java.util.Arrays;

/** At first accidentally read as
 * only using the boundary points of the
 * square.
 */
public class WrongProblem {
	public static void main(String[] args) {
		int n = 5;
		
		// Assume n > 1 for simplicity; n=1 case is 
		// trivial to deal with
		Coordinate[] coords = new Coordinate[4*(n-1)];
		
		for (int i = 1; i < n; i++) {
			coords[4*(i-1) + 0] = new Coordinate(i, 1);
			coords[4*(i-1) + 1] = new Coordinate(n, i);
			coords[4*(i-1) + 2] = new Coordinate(n + 1 - i, n);
			coords[4*(i-1) + 3] = new Coordinate(1, n + 1 - i);
		}

		Arrays.sort(coords);
		
		for (Coordinate c : coords) {
			System.out.println(c);
		}
		
	}

}
