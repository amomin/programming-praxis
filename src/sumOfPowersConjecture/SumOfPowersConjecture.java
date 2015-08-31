package sumOfPowersConjecture;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.HashMap;

/** A straighforward solution, only optimization is to
 * cache powers once calculated (as e.g. suggested in solution posted).
 * 
 * Does not seem to be very effective but does catch the first counter-example
 * (in the 4-5 case) reasonably quickly on a modern computer.
 * 
 * @author amomin
 *
 */
public class SumOfPowersConjecture {

	public static HashMap<Integer, BigDecimal> powers;
	
	public static void main(String args[]) {
		powers = new HashMap<Integer, BigDecimal>();
		int summands = 5;
		int exponent = 6;
		for (int i = 1; i < 400; i++) {
			BigDecimal pow = pow(i,exponent);
			ArrayList<Integer> res = powerSum(pow, i, exponent, summands);
			if (res != null) {
				System.out.println(pow + " is a power sum of exponent "
					+ exponent + " and summands " + summands + ": " + i);
				for (Integer x : res) {
					System.out.println(x);
				}
			}
		}
	}

	/** Attempts to write d as a sum of
	 * "summand"-many perfect powers of "exponent".  Returns
	 * null if cannot be found.
	 * 
	 * Assumes an upperBound on the largest term in the
	 * sum is given (e.g. the exponent-th root of d)
	 * 
	 * @param d
	 * @param upperBound
	 * @param exponent
	 * @param summands
	 * @return list such that the sum of the exponent-th powers of the 
	 * 		elements in the list is equal d, null if not possible with
	 * 		elements <= upperBound.
	 */
	public static ArrayList<Integer> powerSum(BigDecimal d, int upperBound, 
			int exponent, int summands) {
		if (d.compareTo(new BigDecimal(0)) < 0) {
			return null;
		}
		if (summands == 1) {
			int x = intRoot(d, upperBound, exponent);
			BigDecimal pw = pow(x, exponent);
			if (d.equals(pw)) {
				ArrayList<Integer> result = new ArrayList<Integer>();
				result.add(x);
				return result;
			} else { 
				return null;
			}
		} else {
			int y = upperBound;
			while (y >= 1) {
				BigDecimal f = pow(y, exponent);
				ArrayList<Integer> result = powerSum(d.subtract(f), 
					y, exponent, summands - 1);
				if (result != null) {
					result.add(y);
					return result;
				}
				y--;
			}
		}
		return null;
	}

	// Test?
	public static int intRoot(BigDecimal n, int upperBound, int k) {
		for (int x = upperBound; x > 1; x--) {
			BigDecimal d = pow(x, k);
			if (d.compareTo(n) <= 0) {
				return x;
			}
		}
		return 1;
	}
	// Test?
	public static BigDecimal pow(int n, int k) {
		if (powers.containsKey(n)) {
			return powers.get(n);
		}
		BigDecimal d = new BigDecimal(n);
		BigDecimal result = new BigDecimal(1);
		for (int i = 0; i < k; i++) {
			result = result.multiply(d);
		}
		powers.put(n, result);
		return result;
	}
}