package findingTheMedian;

import utilities.Random;
import java.util.Arrays;

public class Examples {
	
	public static void main(String[] args) {
		System.out.println("-------- COMPARE THAT THE TWO SOLUTIONS GIVE THE SAME ANSWER---------");
		for (int i = 0; i < 10; i++) {
			if (!compareTwoSolutions()) System.out.println("DISAGREE ON RUN NUMBER " + i);
			else  System.out.println("PASS: " + i);
		}
		System.out.println("-------- Demo the Bucket Solution ---------");
		demoBS();
		System.out.println("-------- Demo the QuickFind Solution ---------");
		demoQF();
	}

	public static boolean compareTwoSolutions() {
		int N = 100;
		int klo = 7;
		int khi = 10;
		int k = Random.integer(klo, khi);
		int[] ns = new int[k];
		for(int i =0; i < ns.length; i++) {
			ns[i] = (int) (N * Math.random());
		}
		int s1 = FindinTheMedian.solution1(ns);
		int s2 = FindinTheMedian.solution2(ns);
		if (s1 != s2) {
			System.out.println("Medians: (QF - BS)" + s1 + " - " + s2);
			printArr(ns);
			Arrays.sort(ns);
			printArr(ns);
			
		}
		return s1 == s2;
	}

	public static void demoBS() {
		int N = 100;
		int k = 10;
		int[] ns = new int[k];
		for(int i =0; i < ns.length; i++) {
			ns[i] = (int) (N * Math.random());
		}
		int s2 = FindinTheMedian.solution2(ns);
		System.out.println("Median: " + s2);
		printArr(ns);
		Arrays.sort(ns);
		printArr(ns);
	}
	private static void demoQF() {
		int N = 10;
		int k = 10;
		int[] ns = new int[k];
		int[] sorted1 = new int[ns.length];
		int[] sorted2 = new int[ns.length];
		for(int i =0; i < ns.length; i++) {
			ns[i] = (int) (N * Math.random());
		}
		printArr(ns);
		for (int i = 0; i < ns.length; i++) {
			sorted1[i] = FindinTheMedian.quickfind(ns, i + 1);
		}
		Arrays.sort(ns);
		for (int i = 0; i < ns.length; i++) {
			System.out.println ("Element i for i = " + i + ": " + ns[i] + ", " + sorted1[i]);
			if (ns[i] != sorted1[i]) System.out.println("ERROR at index i = " + i);
		}
	}
	private static void printArr(int[] ns) {
		System.out.printf("-------");
		for(int i =0; i < ns.length; i++) {
			System.out.printf("%d, ", ns[i]);
		}
		System.out.printf("--------%n");
	}

}
