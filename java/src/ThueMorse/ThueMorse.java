package ThueMorse;

public class ThueMorse {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub			
		int N = 40;
		/*
		for (int i = 0; i < N; i ++)
		{
			System.out.println("Value at " + i + " is " + valueAt(i));
		}
		*/
		int[] res = computeTo(10);
		for (int i = 0; i < res.length; i ++)
		{
			System.out.println("Value at " + i + " is " +res[i]);
		}
	}
	
	public static int valueAt(int input)
	{
		boolean count = false;;
		while (input > 0)
		{
			if ((input & 1) > 0) count = !count;
			input = input >> 1;
		}
		return count ? 1 : 0;
	}

	public static int[] computeTo(int N)
	{
		int[] result = new int[N + 1];
		result[0] = 0;
		int i = 1;
		int lim = 1;
		while (i <= N)
		{
			if (i >= (lim<<1)) lim = lim << 1;
			result[i] = (result[i - lim] + 1) % 2;
			i++;
		}
		return result;
	}
}
