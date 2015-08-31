package SpiralWrapping;

public class SprialWrapping {

	/** Demonstrates the SprialWrapping Solution
	 * on a fixed input (the one from the problem
	 * statement)
	 * 
	 * @param args
	 */
	public static void main(String[] args) {
		int N = 4;
		int M = 5;
		int[][] arr = new int[M][N];
		
		for(int i = 0; i < M; i++ )
		{
			for(int j = 0; j < N; j ++)
			{
				arr[i][j] = N*i + j + 1;
			}
		}		
		for(int i = 0; i < M; i ++)
		{
			for(int j = 0; j < N; j++)
			{
				System.out.println(arr[i][j]);				
			}
		}
		
		printSpiralWrap(arr);
	}
	
	/** Solution: print the top row in reverse and remove it,
	 * then rotate the whole array clockwise.
	 * 
	 * @param arr
	 */
	public static void printSpiralWrap(int[][] arr)
	{
		boolean doContinue = true;
		while(doContinue)
		{
			arr = printAndRemoveTop(arr);
			if (arr.length < 1)
			{
				doContinue=false;
			} else if (arr[0].length < 1)
			{
				doContinue = false;
			} else 
			{
				arr = rotate(arr);
			}
		}
	}
	
	/** As the name says; returns the result of this process.
	 * Throws an exception if the number of rows or 
	 * columns is zero.
	 * 
	 * @param arr
	 * @return
	 */
	public static int[][] printAndRemoveTop(int[][] arr)
	{
		int M = arr.length;
		if (M < 1) throw new java.lang.IllegalArgumentException();
		int N = arr[0].length;
		if (N < 1) throw new java.lang.IllegalArgumentException();
		
		for (int j = N-1; j>=0; j --)
		{
			System.out.println(arr[0][j]);
		}
		
		int[][] res = new int[M-1][N];
		for (int i = 1; i < M; i++)
		{
			for(int j = 0; j < N; j++)
			{
				res[i-1][j] = arr[i][j]; 
			}
		}
		return res;
	}
	
	/** Returns teh result of "rotating the matrix
	 * clockwise".  Throws an exception if the matrix
	 * has zero columns or zero rows.
	 * 
	 * @param arr
	 * @return
	 */
	public static int[][] rotate(int[][]arr)
	{
		int M = arr.length;
		if (M < 1) throw new java.lang.IllegalArgumentException();
		int N = arr[0].length;
		if (N < 1) throw new java.lang.IllegalArgumentException();		
		int[][]res = new int[N][M];
		for (int i = 0; i < M; i++)
		{
			for (int j = 0; j < N; j++)
			{
				res[j][M-i-1] = arr[i][j];
			}
		}
		return res;
	}

}
