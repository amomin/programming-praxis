package PatienceSorting;

import java.util.*;

public class TestPatienceSorting {
	
	public static void main(String[] args) {
		//test1();
		for (int i = 0; i < 50; i++) {
			testRandom(1000, false);
		}
	}

	public static void test1() {
		//int[] list = {9,3,6,4,3,8,5,1};
		int[] list = {9, 2, 6, 2, 6, 6, 10, 7, 5, 4};

		System.out.println("Input:");
		for (Integer i : list) {
			System.out.println(i);
		}

		System.out.println("Sorted:");
		int[] sorted = PatienceSorting.sort(list, false);
		for (Integer i : sorted) {
			System.out.println(i);
		}

	}
	public static void testRandom(int N, boolean printOut) {
		int[] input = new int[N];

		Random rand = new Random();
		for(int i = 0; i < N; i++) {
			input[i] = rand.nextInt(N) + 1;
		}
		String inputString = new String(); inputString = "";
		for (Integer i : input) {
			inputString += " " + String.valueOf(i);
		}
		if (printOut) {
			System.out.println(inputString);
		}

		if (printOut) {
			System.out.println("Sorted:");
		}
	
		int[] sorted = PatienceSorting.sort(input, false);

		String output = new String();
		output = "";
		for (Integer i : sorted) {
			output += String.valueOf(i) + " ";
		}
		if (printOut) {
				System.out.println(output);
		}
		if (! isSorted(sorted)) {
			System.out.println("Fail!");
		} else {
			System.out.println("Pass");
		}
	}

	private static boolean isSorted(int[] list) {
		if (list.length < 2) return true;
		int prev = list[0];
		for (int i = 1; i < list.length; i++) {
			if (list[i] < prev) return false;
			prev = list[i];
		}
		return true;
	}
}
