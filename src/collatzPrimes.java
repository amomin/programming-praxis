import java.math.BigInteger;
import java.util.HashMap;


public class collatzPrimes {

	public static final int MAX = 5000000;
	public static final int MAXFACTOR = 100;
	
	public static HashMap<Integer, Integer> hm;

	/** We add a cut-off MAX*MAXFACTOR to ensure the
	 * numbers don't get too large.  This prevents
	 * us from needing to count the value for too-large
	 * values (although if MAX is too small an answer
	 * won't be found, or - perhaps - one that is not
	 * the smallest possible).
	 * 
	 * @param args
	 */
	public static void main(String[] args) {
		hm = new HashMap<Integer, Integer>();
		int x = 2;
		int ps = countCollatzPrimes(x);
		while (ps < 65 && x < MAX) {
			x++;
			ps = countCollatzPrimes(x);
			if (ps > 60) {
				System.out.println("Collatz x = " + x 
					+ " has this many primes: " + ps);
			}
			if (x % (MAX/100) == 0) {
				System.out.println("At " + x);
			}
		}
		System.out.println(x + ": " + ps);
	}

	// Just count number of primes in the collatz
	// sequence starting from n.
	public static int countCollatzPrimes(int n) {
		int x = n;
		int primes = 0;
		while (x != 1) {
			/* */
			if (hm.containsKey(x)) {
				int result = primes + hm.get(x); 
				hm.put(n, result);
				return result; 
			}
			if (isPrime(x)) {
				primes++;
			}
			if (x < n) {
				int count = countCollatzPrimes(x);
				hm.put(n, primes + count);
				return primes + count;
			}
			if (x % 2 == 0) {
				x = x/2;
			} else {
				x = 3*x + 1;
			}
			if (x > MAXFACTOR*MAX) return 0;
		}
		hm.put(n, primes);
		return primes;
	}
	
	public static boolean isPrime(int n) {
		BigInteger bi = BigInteger.valueOf(n);
		return bi.isProbablePrime(10);
	}
}
