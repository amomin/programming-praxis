package closestPair1;

import utilities.Pair;
import utilities.Stopwatch;

public class ClosestPairBenchmark {

	public static void main(String args[]) {
		//benchmarkBrute(1000, 4);
		benchmarkXSort(100000, 7);
		// compare();  // Test for correctness against brute force algorithm
	}
	
	public static void compare() {
		Point[] points = generateRandomPoints(5000, 100);
		Pair<Point, Point> p = ClosestPair1.brute(points);
		Pair<Point, Point> q = ClosestPair1.xSort(points);
		System.out.println(p.toString());
		System.out.println(q.toString());
	}
	
	public static void benchmarkBrute(int N, int k) {
		for (int i = 0; i < k; i++) {
			Point[] points = generateRandomPoints(N, 10);
			Stopwatch s = new Stopwatch();
			Pair<Point, Point> p = ClosestPair1.brute(points);
			//System.out.println(p.toString());
			System.out.printf("\nFinished run with " + N + " points");
			s.logStop();
			N *= 2;
		}		
	}
	
	public static void benchmarkXSort(int N, int k) {
		for (int i = 0; i < k; i++) {
			Point[] points = generateRandomPoints(N, 10);
			Stopwatch s = new Stopwatch();
			Pair<Point, Point> p = ClosestPair1.xSort(points);
			s.logStop();
			System.out.println(p.toString());
			System.out.println("Finished run with " + N + " points");
			N *= 2;
		}		
	}
	
	public static Point[] generateRandomPoints(int N, int spacing) {
		Point[] points = new Point[N];
		for (int i = 0; i < N; i++) {
			int x = (int)(Math.random()*N*spacing);
			int y = (int)(Math.random()*N*spacing);
			points[i] = new Point(x,y);
		}
		return points;
	}
}
