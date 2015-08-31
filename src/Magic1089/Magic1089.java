package Magic1089;

public class Magic1089 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {

		assert(args.length == 1);		
		int x = Integer.parseInt(args[0]);		
		assert(isThreeDigits(x));
		assert(isDigitDescending(x));
		
		if (!isThreeDigits(x))
		{
			throw new java.lang.IllegalArgumentException("Input must have 3 digits");
		}
		if (!isDigitDescending(x))
		{
			throw new java.lang.IllegalArgumentException("Input must have descending digits");			
		}
		
		int reversed = reverse(x);
		int diff = x - reversed;
		reversed = reverse(diff);
		System.out.println(diff + reversed);
	}
	
	private static boolean isThreeDigits(int n)
	{
		return n > 99 && n < 1000;
	}

	private static boolean isDigitDescending(int n)
	{
		int x = n / 100;
		int y = (n / 10) % 10;
		int z = n % 10;
		return (x > y) && (y > z);
	}
	
	/** Reverses a 3 digit integer
	 * 
	 * @param x
	 */
	private static int reverse(int n)
	{
		int x = n / 100;
		int y = (n / 10) % 10;
		int z = n % 10;		
		return 100*z + 10*y + x;
	}
}
