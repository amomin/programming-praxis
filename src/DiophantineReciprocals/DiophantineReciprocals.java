package DiophantineReciprocals;

public class DiophantineReciprocals {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		bruteForce(0, 400, false);
		long duration = System.currentTimeMillis() - start;
		System.out.println(System.out.printf("Duration was %d ms:", duration));
	}

	/** Brute force solution
	 * 
	 * Loop through all longegers, counting solutions
	 * until number exceeds N (minus 1).
	 * 
	 * @param N long limit to test
	 * @param doPrint Whether to Print solution sets
	 */
	public static void bruteForce(long n, long N, boolean doPrint) {
		long count = 0;
		while (count < N) {
			count = numPairs(n, doPrint);
			n++;
			if (doPrint)
				System.out.println(n-1 + ": " + count);		
		}
		System.out.println(n-1 + ": " + count);		
	}
	public static void bruteForce(long N, boolean doPrint) {
		bruteForce(0, N, doPrint);
	}
	public static void bruteForce(long N) {
		bruteForce(N, false);
	}

	/**
	 * Brute count of number of solutions to
	 * 1/x + 1/y = 1/n
	 * 
	 * <p>
	 * Suppose x < y.  Then x is between n+1 and 2*n.  The
	 * value of x,n determine y.  Find y and check if x,y,n solve;
	 * increment if they do.
	 * 
	 * Solution is O(n).
	 * </p>
	 * 
	 * @param n - the n in the equation 
	 * @return number of solutions to the equation
	 */
	public static long numPairs(long n, boolean doPrint) {
		long y;
		long count = 0;
		for (long x = n + 1; x <= 2*n; x++) {
			y = (long) (n*x)/(x - n);
			if (n*(x+y) == x*y) {
				if (doPrint) {
					System.out.printf("1 / %d + 1 / %d.\n",x,y);					
				}
				count++;
			}
		}
		return count;
	}
	public static long numPairs(long n) {
		return numPairs(n, false);
	}
}