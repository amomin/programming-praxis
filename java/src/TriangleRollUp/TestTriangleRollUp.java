package TriangleRollUp;

import java.util.ArrayList;

public class TestTriangleRollUp {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int N = 10;
		String[] inpt = new String[N];
		for (int i = 0; i < N; i++)
		{
			int r = (int) (Math.random() * N);
			inpt[i] = (new Integer(r)).toString();
		}
		TriangleRollUp.main(inpt);
	}

}
