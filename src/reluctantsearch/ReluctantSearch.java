package reluctantsearch;

public class ReluctantSearch {

	// Totally not thread-safe, just to make sure it
	// takes 2n+1 time as promised (except perhaps when
	// a value is repeated)
	private volatile static int depth = 0;

	/** Example
	 */
	public static void main(String[] args) {
		int[] arr = {1,3,7,8,22,22,34,45,67,123,234};
		int x;

		x = 1;
		System.out.println(x + ", " + research(arr, x));
		System.out.println("Depth: " + depth);
		x = 5;
		System.out.println(x + ", " + research(arr, x));
		System.out.println("Depth: " + depth);
		x = 9;
		System.out.println(x + ", " + research(arr, x));
		System.out.println("Depth: " + depth);
		x = 22;
		System.out.println(x + ", " + research(arr, x));
		System.out.println("Depth: " + depth);
		x = 122;
		System.out.println(x + ", " + research(arr, x));
		System.out.println("Depth: " + depth);
		x = 123;
		System.out.println(x + ", " + research(arr, x));
		System.out.println("Depth: " + depth);
		x = 234;
		System.out.println(x + ", " + research(arr, x));
		System.out.println("Depth: " + depth);
		x = 255;
		System.out.println(x + ", " + research(arr, x));
		System.out.println("Depth: " + depth);
	}
	/** Returns the index of x in arr, -1 if x is not in arr
	 * 
	 * @param arr
	 * @param x
	 * @return
	 * @throws java.lang.IllegalArgumentException
	 */
	public static int research(int[] arr, int x)
		throws java.lang.IllegalArgumentException {
		depth = 0;
		for (int i = 0; i < arr.length - 2; i++) {
			if (arr[i] > arr[i+1]) {
				throw new java.lang.IllegalArgumentException();
			}
		}
		return research(arr, x, 0, arr.length - 1);
	}
	/** Returns the index of x in arr if
	 * between i and j (inclusive), -1 if x is not 
	 * in arr (in this range)
	 * 
	 * If I weren't lazy I might implement as a loop.
	 * 
	 * @param arr
	 * @param x
	 * @param i
	 * @param j
	 * @return
	 */
	protected static int research(int[] arr, int x, int i, int j) {
		depth++;
		if (i < 0) throw new java.lang.IllegalArgumentException();
		if (j >= arr.length) throw new java.lang.IllegalArgumentException();
		if (i > j) return -1;
		if (i == j) return (arr[i] == x)? i : -1;
		int m = (i + j) / 2;
		
		if (x <= arr[m]) {
			int k = research(arr, x, m+1, j);
			if (k == -1) {
				return research(arr, x, i, m);
			} else {
				return k;
			}
		} else {
			int k = research(arr, x, i, m);
			if (k == -1) {
				return research(arr, x, m+1, j);
			} else {
				return k;
			}
		}
	}
}
