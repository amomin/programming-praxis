package TornNumbers;

import java.util.ArrayList;

/*
 * This solution misses possible "solutions" with "leading zeros" e.g.
 *
 * 9801 = (98+01)^2 = 98 + 01
 * or
 * 10000 = (100 + 0)^2 = 100 "+" 00
 */

/**
 * Torn Numbers - finds "torn numbers"
 *
 * <p>
 * In 1917, Henry Ernest Dudeney published a book Amusements in Mathematics of arithmetic puzzles. Today’s exercise solves puzzle 113 from that book:
 *
 * A number n is a torn number if it can be chopped into two parts which, when added together and squared, are equal to the original number. For instance, 88209 is a torn number because (88 + 209)2 = 2972 = 88209.
 *
 * Your task is to write a program to find torn numbers. When you are finished, you are welcome to read or run a suggested solution, or to post your own solution or discuss the exercise in the comments below.
 * </p>
 *
 * <p>
 * See
 * http://programmingpraxis.com/2014/09/16/torn-numbers/
 * </p>
 */

public class TornNumbers {

	/** Compute torn numbers less than N -
	 *
	 * this algorithm misses answers with "leading zeros"
	 *
	 * @param int N - check integers from 0 to N
	 */
	public static ArrayList<TornNum> attempt1(int N) {
		int i = 1;
		int j = 1;
		int n;
		int concat;
		int numDigits = 1;
		ArrayList<TornNum> tornNumbers = new ArrayList<TornNum>();
		while (i*i < N) {
			j = 1;
			n = i+j;
			while (n * n < N) {
				concat = ((int) Math.pow(10,numDigits))*i + j;
				if (concat == n * n) {
					tornNumbers.add(new TornNum(n*n, i, j));
				}
				j++;
				n = i + j;
				numDigits = 1 + (int) Math.floor(Math.log10(j));
			}
			i++;
		}
		return tornNumbers;
	}

	/** Compute torn numbers less than N -
	 *
	 * @param int N - check integers from 0 to N
	 */
	public static ArrayList<TornNum> allLessThan(int N) {
		int n = 1;
		int M = 1;
		int numDigits = 1;
		int digit;
		int i,j, mod;
		ArrayList<TornNum> tornNumbers = new ArrayList<TornNum>();
		while (M < N) {
			digit = 0;
			while (digit <= numDigits) {
				mod = (int)Math.pow(10,digit);
				i = M / mod;
				j = M % mod;
				if ( (i+j)*(i+j) == M ) {
					tornNumbers.add(new TornNum(M, i, j));
				}
				digit++;
			}
			n++;
			M = n*n;
			numDigits = 1 + (int) Math.floor(Math.log10(M));
		}
		return tornNumbers;
	}

	public static void main(String[] args) {
		int N = 1000000000;
		ArrayList<TornNum> tn = allLessThan(N);
		for (TornNum i : tn) {
			System.out.println(i.asString());
		}
	}

	private static class TornNum {
		private int i;
		private int j;
		private int n;

		public TornNum(int num, int a, int b) {
			i = a;
			j = b;
			n = num;
		}

		public String asString() {
			int numDigits = 1 + (int) Math.floor(Math.log10(j));
			int concat =  + j;
			return String.format("%12d = (%d + %d)^2 = %d + %d",
					n, i, j, ((int) Math.pow(10,numDigits))*i, j);
		}
	}
}
