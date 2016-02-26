package closestPair1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

import utilities.Pair;
import utilities.Stopwatch;

public class ClosestPair1 {

	public static void main(String[] args) throws FileNotFoundException {

		String path = Config.PATH + "points1.txt";
		Scanner scanner = new Scanner(new File(path));
		ArrayList<Point> pointlist = new ArrayList<Point>();
		
		while (scanner.hasNextInt()) {
			int x = scanner.nextInt();
			if (scanner.hasNextInt()) {
				int y = scanner.nextInt();
				pointlist.add(new Point(x,y));
			} else {
				break;
			}
		}
		
		Point[] points = new Point[0]; 
		points = pointlist.toArray(points);

		Stopwatch s = new Stopwatch();
		//brute(points);
		Pair<Point, Point> pair = xSort(points);
		long duration = s.stop();
		
		Point m1 = pair.left();
		Point m2 = pair.right();
		System.out.printf("\nClosest points are p = %s, q = %s with distance %.3f\n", 
				m1.toString(), m2.toString(), Math.sqrt(m1.distSq(m2)));
		System.out.printf("\nTook %d milliseconds\n", duration);
	}
	
	/** Another slightly better strategy - sort by x coordinate, and
	 * consider points in that order.  Precompute the
	 * x-squared distance: if too large, go on to 
	 * next iteration of outer loop.  This should allow to
	 * discard many comparisons when the list is large (unless
	 * the set is structured quite specially).
	 * 
	 * @param points
	 */
	public static Pair<Point, Point> xSort(Point[] points) {
		if (points.length < 2) throw new IllegalArgumentException();
		Arrays.sort(points, Point.xComparison);
		Point m1 = points[0];
		Point m2 = points[1];
		long min = m1.distSq(m2);
		for (int i = 0; i < points.length - 1; i++) {
			for (int j = i + 1; j < points.length; j++) {
				long xdistsq = (points[i].x() - points[j].x());
				xdistsq = xdistsq * xdistsq;
				if (xdistsq >= min || xdistsq <= 0) break;
				long distSq = points[i].distSq(points[j]);
				if (distSq < min) {
					min = distSq;
					m1 = points[i];
					m2 = points[j];
				}
			}
		}
		Pair<Point, Point> pair = new Pair<Point, Point>(m1, m2);
		return pair;
	}
	
	public static Pair<Point, Point> brute(Point[] points) {
		if (points.length < 2) throw new IllegalArgumentException();
		
		long min = -1;
		Point m1 = new Point(0,0);
		Point m2 = new Point(0,0);
		for (Point p : points) {
			for (Point q : points) {
				if (!p.equals(q) && (min < 0 || min > p.distSq(q)) ) {
					min = p.distSq(q);
					m1 = p;
					m2 = q;
				}
			}
		}
		Pair<Point, Point> pair = new Pair<Point, Point>(m1, m2);
		return pair;
	}	
}
