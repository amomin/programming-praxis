package utilities;

public class Pair<Left, Right> {

	Left left;
	Right right;
	
	public Pair(Left l, Right r) {
		left = l;
		right = r;
	}
	
	public Left left() {
		return left;
	}
	
	public Right right() {
		return right;
	}
	
	public String toString() {
		return "(" + left.toString() + ", " + right.toString() + ")";
	}
}
