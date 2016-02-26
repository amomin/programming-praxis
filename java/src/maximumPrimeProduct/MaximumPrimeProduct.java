package maximumPrimeProduct;

import java.math.BigInteger;

public class MaximumPrimeProduct {

	public static void main(String[] args) {
		for (int i = 10000; i < 10100; i++) {
			System.out.printf("Int %4d - value: %5d %n", i, solution(i));
		}
	}

	/** 
	 * @param N
	 * @return
	 */
	public static int solution(int N) {
		int n = 2;
		int upperBound = (int) Math.sqrt(N);
		int maxSoFar = 0;
		while(n < upperBound) {
			if (isPrime(n)) {
				int m = N/n;
				while (m*n > maxSoFar) {
					if (isPrime(m)) {
						maxSoFar = m*n;
						m = 0;
					}
					m--;
				}
			}
			n++;
		}
		return maxSoFar;
	}

	private static Boolean isPrime(int n) {
		BigInteger x = BigInteger.valueOf(n);
		return x.isProbablePrime(10);
	}
}
