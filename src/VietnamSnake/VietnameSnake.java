package VietnamSnake;

public class VietnameSnake {

	public static void main(String[] args) {
		for(int i = 0; i < 9*9*9*9*9; i++) {
			int[] arr = new int[9];
			int x = i;
			for (int d = 0; d < 5; d++) {
				arr[d] = (x % 9) + 1;
				x /= 9;
			}
			for(int j = 0; j < 9*9*9*9; j++) {
				int y = j;
				for (int d = 0; d < 4; d++) {
					arr[d+5] = (y % 9) + 1;
					y /= 9;
				}
				
				int val = evaluate(arr);
				if (val == 66) {
					boolean doprint = true;
					String toprint = "";
					for (int k = 0; k < 9; k++) {
						if (k > 0) {
							toprint = toprint + ", " + arr[k];
							//if (arr[k] < arr[k-1]) doprint = false;
						} else {
							toprint = " " + arr[k];
						}
					}
					if (doprint) System.out.printf("%s%n",toprint);
				}
			}
		}
	}
	public static int evaluate(int[] arr) {
		// If you only want integral solutions
		if (13*arr[1] % arr[2] != 0) return -1; 
		if (arr[6]*arr[7] % arr[8] != 0) return -1;
		
		return arr[0] + (13*arr[1] / arr[2]) 
			+ arr[3] + 12*arr[4] - arr[5] 
			- 11 + (arr[6]*arr[7]/arr[8]) - 10;
	}
}
