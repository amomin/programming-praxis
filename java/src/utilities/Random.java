package utilities;

public class Random {

	// From zero to hi inclusive
	public static int integer(int hi) {
		return integer(0,hi);
	}
	// From lo to hi inclusive
	public static int integer(int lo, int hi) {
		return lo + (int) (Math.random()*(1 + hi - lo));
	}
	public static int[] intArray(int size, int hi) {
		return intArray(size, 0, hi);
	}
	public static int[] intArray(int size, int lo, int hi) {
		int[] res = new int[size];
		for (int i = 0; i < size; i++) {
			res[i] = integer(lo, hi);
		}
		return res;
	}
	
	// From zero to hi
	public static double dble(double hi) {
		return dble(0,hi);
	}
	// From lo to hi
	public static double dble(double lo, double hi) {
		return lo + Math.random()*(hi - lo);
	}
}
