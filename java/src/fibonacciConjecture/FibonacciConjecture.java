package fibonacciConjecture;

import java.math.BigInteger;

/** Problem not yet solved - find a counter-example
 * to the claim that for every Fibonacci number F,
 * F*F + 41 is composite
 * 
 * @author amomin
 *
 */
public class FibonacciConjecture {

	public static void main(String[] args) {
		brute();
	}
	
	public static void brute() {
		final boolean DEBUG = false;
		final int MAXITER = 12600;
		final int STARTTESTING = 12580; // Otherwise takes a 
			// fair amount of time (hours)
			// Miller-Rabin test is the bottle-neck
			// because the numbers F*F + 41 quickly become
			// very large
		
		long STARTTIME = System.currentTimeMillis();
		
		BigInteger f0 = BigInteger.ONE;
		BigInteger f1 = BigInteger.ONE;
		
		for (int i = 2; i < MAXITER; i++) {
			f1 = f1.add(f0);
			f0 = f1.subtract(f0);
			if (i % 12 == 11	// mod 2, 3 restrictions
					&& (i % 60 != 23 && i % 60 != 35) // mod 5 restrictions
					&& i > STARTTESTING) {
				BigInteger t = f1.pow(2).add(BigInteger.valueOf(41));
				if (isPrime(t)) {
					System.out.println(f1.toString());
					System.out.printf("\nFibbonacci number %d \n", i);
					break;
				}
				if (DEBUG) {
					System.out.printf("%s, %s, %s \n", f0.toString(), 
							f1.toString(), 
							t.toString());
					System.out.printf("i is %d: %s, %s, %s \n", 
							i,
							t.mod(BigInteger.valueOf(2)).toString(), 
							t.mod(BigInteger.valueOf(3)).toString(), 
							t.mod(BigInteger.valueOf(5)).toString());					
				}
			}
		}
		System.out.printf("\tElapsed time: %ds\n", 
				(System.currentTimeMillis() - STARTTIME)/1000);
	}
	public static boolean isPrime(BigInteger x) {
		return x.isProbablePrime(2);	//Implementation of Miller-Rabin
	}
}