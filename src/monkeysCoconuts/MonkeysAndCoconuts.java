package monkeysCoconuts;

import java.math.BigInteger;

/** Originally solved it using solutions 1 and 2 as a
 * slightly complicated recurrence relation among 3 
 * variables.
 * 
 * After reading the posted answers, this is a just simple
 * first order (non-homogeneous) recurrence relation,
 * with non-homogeneous term solved by const 1 - n.
 * Following that one gets a nice simple formula for the 
 * answer - see solution 3. It also demonstrates and 
 * explains why 1-n * is "(actually) the right" answer :)
 * 
 * (Which also reminded me that I had solved this problem, 
 * in exactly the way of solution3, long ago as an undergrad.)
 * 
 * @author amomin
 *
 */
public class MonkeysAndCoconuts {

	public static void main(String[] args) {
		for (int i = 2; i < 31; i++) {
			System.out.println("For case i = " + i);
			solution2(i);
			BigInteger s3 = solution3(i);
			System.out.println("Solution = " + s3);
		}
	}
	
	/** long Solution - only works to about
	 * n = 9(?) - but implemented with BigInteger
	 * for larger n.  Keeping this because it is quite
	 * different (though not better) than posted solutions.
	 * 
	 * Strategy is this: 
	 * Let s_k  be the number of coconuts left after the 
	 * kth-last-to-wake sailor.
	 * Write the recurrence relation in fractional form as such:
	 * 
	 * s_{k+1} = (a_1*s_k + b_1)/c_1
	 * s_{k+2} = (a_2*s_k + b_2)/c_2
	 * s_{k+3} = (a_3*s_k + b_3)/c_3
	 * etc..
	 * Then we find that
	 * a_{k+1} = n * a_k
	 * b_{k+1} = n * b_k + (n-c) * c_k
	 * c_{k+1} = (n-1) * c_k
	 * which we can easily solve for a = a_n, b=b_n, c=c_n 
	 * (taking initially a_0 = c_0 = 1, b_0 = 0)
	 * giving us a formula
	 * 
	 * s_n = (a*C + b)/c
	 * 
	 * Where C = k*n is the final number of coconuts.
	 * Then we need only that s_n is an integer, or
	 * a*C + b % c == 0
	 * i.e. solve the congruence relation
	 * (a*n)*k + b % c == 0
	 */
	public static long solution1(int n) {
		long a = 1;
		long b = 0;
		long c = 1;
		for (int i = 0; i < n; i++) {
			a = n * a;
			b = n * b + (n-1) * c;
			c = (n-1) * c;
		}
		// Bottle neck:
		// Solve ak = -b (mod c)
		long k = solve(n*a, b, c);
		long l = n*k;
		long answer = l;
		System.out.println("Final number of coconuts is " + l + " / " + n);
		for (int i = 0; i < n; i++) {
			l = (n * l)/(n-1) + 1;
		}
		System.out.println("Original number of coconuts is " + l);
		return answer;
	}

	/** Same strategy as solution1 but using BigInteger
	 * and referencing a congruence solver linSolve2
	 * rather than "guess and check".
	 * 
	 * @param n
	 * @return
	 */
	public static BigInteger solution2(int n) {
		BigInteger bn = BigInteger.valueOf(n);
		BigInteger bnminus1 = BigInteger.valueOf(n-1);
		BigInteger ba = BigInteger.valueOf(1);
		BigInteger bb = BigInteger.valueOf(0);
		BigInteger bc = BigInteger.valueOf(1);
		for (int i = 0; i < n; i++) {
			ba = ba.multiply(bn);
			bb = bb.multiply(bn).add(bc.multiply(bnminus1));
			bc = bc.multiply(bnminus1);
		}
		// Note that this is the bottleneck
		//BigInteger bk = linSolve1(ba.multiply(bn, bb, bc); // Guess and check
		BigInteger bk = linSolve2(ba.multiply(bn), bb, bc); // Actually solve
		BigInteger bl = bn.multiply(bk);
		BigInteger answer = bl;
		System.out.println("Final number of coconuts is " + bl + " / " + n);
		for (int i = 0; i < n; i++) {
			bl = ((bl.multiply(bn)).divide(bnminus1)).add(BigInteger.ONE);
		}
		System.out.println("Original number of coconuts is " + bl);
		return answer;
	}

	/** Just spit out the solution to the first order
	 * recurrence relation (with particular solution
	 * c_k = 1 - n and general homogeneous solution
	 * c_k = c_0 * a^k)
	 * 
	 * c_{k+1} = a*c_k - a,	    where a = (n-1)/n
	 * 
	 * @param n
	 * @return
	 */
	public static BigInteger solution3(int n) {
		BigInteger bnminus1 = BigInteger.valueOf(n - 1);
		BigInteger bn = BigInteger.valueOf(n);
		if (n % 2 == 1) {
			return (bn.pow(n)).subtract(bnminus1);
		} else {
			return ((bn.pow(n)).multiply(bnminus1)).subtract(bnminus1);
		}
	}
	
	// Need to solve a*k = - b (mod c)
	// Need to solve k = -b/a (mod c)
	// Incrementing k no good if c is large
	// A primitive root would help!
	private static long solve(long a, long b, long c) {
		long k = 1;
		long lmod = (a*k + b) % c;
		while (((lmod) % c) != 0) {
			k++;
			//lmod = a*k + b;
			lmod = (lmod + a) % c;
		}
		//System.out.println(k);
		return k;
	}

	// Solve x*a = 1 (mod c)
	private static long invert(long a, long c) {
		return 1;
	}

	// Solve ak + b == 0 mod c
	// Trivial solution method (guess and check), but takes very long
	private static BigInteger linSolve1(BigInteger ba, BigInteger bb,
		BigInteger bc) {
		BigInteger bk = BigInteger.valueOf(1);
		BigInteger lmod = (ba.multiply(bk)).add(bb);
		while (!(lmod.mod(bc)).equals(BigInteger.ZERO)) {
			bk = bk.add(BigInteger.ONE);
			lmod = (lmod.add(ba)).mod(bc); // Prevent from getting too large
		}
		return bk;
	}
	
	// Solve ak + b == 0 mod c
	// The "correct" way - actuallly "solve" the linear congruence
	// Fortunately the inversion method is provided by
	// BigInteger
	private static BigInteger linSolve2(BigInteger ba, BigInteger bb,
		BigInteger bc) {
		BigInteger lhs = (bb.negate()).mod(bc);
		BigInteger bk = (lhs).multiply(ba.modInverse(bc));
		return bk.mod(bc);
	}
}