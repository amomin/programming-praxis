package BlumsMentalHash;

import java.util.ArrayDeque;

public class BlumsMentalHash {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String toEncode = "abc";
		
		System.out.println("Input: " + toEncode);
		
		DigitMap f = new DigitMap("83732340156234964091782345");
		int[] permList = {0,2,9,8,7,3,6,5,1,4};
		PermutationOf10 g = new PermutationOf10(permList);
		
		ArrayDeque<Integer> asDigits = f.encode(toEncode);
		ArrayDeque<Integer> result = new ArrayDeque<Integer>();
		
		int first = asDigits.removeFirst();
		if (! asDigits.isEmpty())
		{
			int last = asDigits.peekLast();
			first = (first + last) % 10;
		}
		int pos = g.inv(first);
		first = g.val(pos + 1) % 10;
		result.addLast(first);
		
		int prev = first;
		while(! asDigits.isEmpty())
		{
			int next = asDigits.removeFirst();
			pos = g.inv((prev + next) % 10);
			next = g.val((pos + 1) % 10);
			result.addLast(next);
			prev = next;
		}
		
		System.out.println("Result: " + result);
	}

	/** Simple model of for a Permutation of 10
	 * (as a bijection)
	 * 
	 * @author user
	 */
	public static class PermutationOf10
	{
		int[] permutation;
		
		/** Input is an array where the ith entry
		 * is assumed to be the value of the permutation 
		 * at the index i (considered as a bijection).
		 * 
		 * @param _permutation
		 */
		public PermutationOf10(int[] _permutation)
		{
			if (! isPermutationOf10(_permutation)) // Make sure it is a permutation
			{
				throw new java.lang.IllegalArgumentException("Must be a permutation");
			}			
			permutation = _permutation;
		}

		public static boolean isPermutationOf10(int[] list)
		{
			boolean[] digitshit = new boolean[10];
			for (int x : list)
			{
				if (x < 0 || x > 9)
				{
					throw new java.lang.IllegalArgumentException("All digits must be between 0 and 9");
					//return false;
				}
				digitshit[x] = true;
			}
			for (boolean b : digitshit)
			{
				if (!b) return false;
			}
			return true;
		}
		
		/** Value y of the permutation on the input x i.e. y = g(x)
		 * 
		 */
		public int val(int x)
		{
			if (x < 0 || x > 9)
			{
				throw new java.lang.IllegalArgumentException("Input must be between 0 and 9");
			}
			return permutation[x];
		}
		
		/** Inverse x of the permutation at value y (i.e. g(x) = y)
		 * 
		 * @param y
		 * @return
		 */
		public int inv(int y)
		{
			if (y < 0 || y > 9)
			{
				throw new java.lang.IllegalArgumentException("Input must be between 0 and 9");
			}
			int x = 0;
			while(x < 10)
			{
				if (val(x) == y) return x;
				x++;
			}
			throw new java.lang.ArithmeticException("Failed to compute inverse permutation at " + y);
			}
			
		}

	/** Models the Digit map of a string (mapping of the alphabet
	 * to digits from 0-9).
	 * 
	 * @author user
	 *
	 */
	public static class DigitMap
	{
		String s;

		public DigitMap(String s)
		{
			if (s.length() != 26) 
			{
				throw new java.lang.IllegalArgumentException("Must have 26 digits");
			}
			if (s.matches("/[^0-9]/"))
			{
				throw new java.lang.IllegalArgumentException("Must enter digits only");				
			}
			this.s = s;
		}
		
		public ArrayDeque<Integer> encode(String toEncode)
		{
			ArrayDeque<Integer> asDigits = new ArrayDeque<Integer>();			
			for(int i = 0; i < toEncode.length(); i ++)
			{
				char c = toEncode.charAt(i);
				int digit = getDigit(c);
				asDigits.addLast(digit);
			}
			return asDigits;			
		}
		
		/**
		 * 
		 * @param x - must be an alphabetical character (else throws IllegalArgumentException)
		 * @return The letters position (between 0 and 25)
		 */
		public int getDigit(char x)
		{
			if ((x >='a' && x <='z') || (x>='A' && x <= 'Z'))
			{				
				int pos =  ((int) Character.toLowerCase(x)) - 97;
				return Integer.parseInt(Character.toString(s.charAt(pos)));
			}
			else {
				throw new java.lang.IllegalArgumentException("Character must be alphabetical");
			}
		}
	}
}
