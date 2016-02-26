package orderedCartesianCoordinates;

public class Coordinate implements Comparable<Coordinate> {

	private int x;
	private int y;
	
	public Coordinate(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public int x() {
		return x;
	}
	
	public int y() {
		return y;
	}

	@Override
	public int compareTo(Coordinate that) {
		return Integer.compare(this.x * this.y, that.x * that.y);
	}
	
	public String toString() {
		return "(" + this.x + ", " + this.y + ")";
	}
	
}
