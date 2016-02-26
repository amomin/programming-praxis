package sumOfFourPrimes;

import java.math.BigInteger; // For Miller-Rabin test
import java.util.ArrayList; // For prime table

/** The posted solution uses the 
 * Goldbach conjecture, which I had not thought about.
 * However, this should effectively act in almost the same
 * way; it should effectively find a solution with the first
 * two taken as 2,2 or 2,3 (odd vs even).  The latter
 * will be slow because it has to reject the 2,2 pair
 * which a simple parity argument could have determined.
 * However this functions pretty quickly already.
 * 
 * @author amomin
 *
 */
public class SumOfFourPrimes {

	public static void main(String[] args) {
		int n = 9000; // n between 7 and 10,000,000		
		System.out.println("N = " + n);
		find(n);
	}

	public static void find(int n) {
		Integer[] primeTable = primeTable(n / 2);
		System.out.println("Prime table tabulated, continuing...");
		for (Integer p : primeTable) {
			if (sumOfThree(n - p, p, primeTable)) {
				System.out.println("Found");
				return;
			}
		}
	}
	
	private static boolean sumOfThree(int sum, int prev, Integer[] primeTable) {
		for (Integer p : primeTable) {
			if (p < prev) {
				continue;
			}
			else {
				if (sumOfTwo(sum - p, p, primeTable)) {
					System.out.printf("%d, %d\n", p, prev);
					return true;
				}
			}
		}
		return false;
	}
	
	private static boolean sumOfTwo(int sum, int prev, Integer[] primeTable) {
		for (Integer p : primeTable) {
			if (p < prev) {
				continue;
			} else {
				if (isPrime(sum - p)) {
					System.out.printf("Primes %d, %d, ", sum - p, p);
					return true;
				}				
			}
		}
		return false;
	}
	
	public static Integer[] primeTable(int N) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		for (int i = 2; i < N; i++) {
			if (isPrime(i)) {
				list.add(i);
			}
		}
		Integer[] res = new Integer[list.size()];
		list.toArray(res);
		return res;
	}
	
	/** Miller-Rabin from the BigInteger class,
	 * but to save time first check a few small primes.
	 * 
	 * @param n
	 * @return
	 */
	public static boolean isPrime(int n) {
		int[] smallPrimes = {2, 3, 5, 7 , 11, 13, 17, 19, 23};
		for (Integer p : smallPrimes) {
			if (n == p) return true;
			if (n % p == 0) return false;
		}
		if (n < 29) return true;
		return BigInteger.valueOf(n).isProbablePrime(10);
	}
}
