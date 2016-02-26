package GeneratingPalindromes;

import java.util.ArrayList;

public class GeneratingPalindromes {

	/** Generates palindromic numbers less than input N.
	 * 
	 * @param int N - upper bound for palindromic numbers in output list
	 * @return an ArrayList of Integers consisting of all non-negative palindromic
	 * 		numbers less than N
	 */
	public static ArrayList<Integer> generatePalindromesLessThan(int N) {
		int powerOfTen = 10;
		ArrayList<Integer> palindromes = new ArrayList<Integer>();
		int n = 0;
		int next = 0;
		palindromes.add(next);
		while (next < N) {
			n = powerOfTen / 10;
			next = makeOddPalindrome(n);
			while (next <= N && n < powerOfTen) {
				palindromes.add(next);
				n++;
				next = makeOddPalindrome(n);
			}
			next = makeOddPalindrome(n-1);
			if (next < N) {
				n = powerOfTen / 10;
				next = makeEvenPalindrome(n);
				while (next < N && n < powerOfTen) {
					palindromes.add(next);
					n++;
					next = makeEvenPalindrome(n);
				}				
			}
			powerOfTen *= 10;
			next = makeEvenPalindrome(n-1);
		}
		return palindromes;
	}

	private static int makeOddPalindrome(int n) {
		int middleDigit = n % 10;
		n /= 10;
		int powerOfTen = 1;
		while (powerOfTen <= n) {
			powerOfTen*=10;
		}
		return n*powerOfTen*10 + middleDigit*powerOfTen + reverse(n);
	}
	
	private static int makeEvenPalindrome(int n) {
		int powerOfTen = 1;
		while (powerOfTen <= n) {
			powerOfTen*=10;
		}
		return n*powerOfTen + reverse(n);
	}

	/** Reverses the digits of an integer n.
	 * 
	 * @param n - int n = the integer to reverse
	 * @return the integer with digits of n reverse
	 */
	private static int reverse(int n) {
		int result = 0;
		int place = 1;
		int digit;
		while (n > 0) {
			digit = n % 10;
			result = 10*result + digit;
			n/=10;
			place*=10;
		}
		return result;
	}
	
	/**
	 * Returns the nth palindromic number. 
 	 *
	 * @param index in the list of palindromic numbers
	 * @return nth largest palindromic number
	 */
	public static int palindromicNumber(int n) {
		if (n < 2) return n;
		int powerOfTen = 1;
		while (powerOfTen < n) {
			powerOfTen *= 10;
		}
		int num = n - powerOfTen/10;
		int leadingDigit = n / (powerOfTen/10);
		if (leadingDigit > 1) {
			return makeOddPalindrome(num);
		}
		return makeEvenPalindrome(num);
	}

	public static void main(String[] args) {
		// Method one, control the largest element
		// in the output list
		ArrayList<Integer> palindromes = generatePalindromesLessThan(100000);
		int count = 1;
		for(Integer p : palindromes) {
			System.out.println("Palindrome number " + count + " is " + p);
			count++;
		}
		// Method two, control the size of the output list
		int q;
		for (int i = 0; i < 1000; i++) {
			q = palindromicNumber(i);
			System.out.println("Palindrome number " + i + " is " + q);
		}
	}
}
