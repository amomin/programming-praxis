package closestPair1;

import java.util.Comparator;

public class Point {
	private int x;
	private int y;
	
	public Point(int _x, int _y) {
		x = _x;
		y = _y;
	}

	public int x() {
		return x;
	}
	
	public int y() {
		return y;
	}
	
	public static Comparator<Point> xComparison 
		= new Comparator<Point>() {
		public int compare(Point p, Point q) {
			if (p.x < q.x) return -1;
			if (p.x > q.x) return 1;
			return 0;
		}
	};
	
	public long distSq(Point that) {
		long deltax = (long)(x - that.x);
		long deltay = (long)(y - that.y);
		return deltax*deltax + deltay*deltay;
	}
	
	public String toString() {
		return "(" + x + "," + y + ")";
	}
}
