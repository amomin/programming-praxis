package identifyingAnagrams;

import static org.junit.Assert.*;

import org.junit.Test;

public class IdentifyingAnagramsTest {

	private String[][] trueCases() {
		String[][] result = new String[5][2];
		result[0][0] = "";
		result[0][1] = "";
		result[1][0] = "a";
		result[1][1] = "a";
		result[2][0] = "ab";
		result[2][1] = "ab";
		result[3][0] = "ab";
		result[3][1] = "ba";
		result[4][0] = "aa";
		result[4][1] = "aa";
		return result;
	}
	private String[][] falseCases() {
		String[][] result = new String[9][2];
		result[0][0] = "a";
		result[0][1] = "b";
		result[1][0] = "aa";
		result[1][1] = "ab";
		result[2][0] = "aa";
		result[2][1] = "ba";
		result[3][0] = "ab";
		result[3][1] = "bb";
		result[4][0] = "aa";
		result[4][1] = "ab";
		result[5][0] = "abc";
		result[5][1] = "abd";
		result[6][0] = "abb";
		result[6][1] = "aba";
		result[7][0] = "abbb";
		result[7][1] = "abbba";
		result[8][0] = "abbba";
		result[8][1] = "abbb";
		return result;
	}
	@Test
	public void testSolution1() {
		String[][] truecases = trueCases();
		String[][] falsecases = falseCases();
		for (int i = 0; i < truecases.length; i++) {
			assertTrue(IdentifyingAnagrams.solution1(truecases[i][0],
				truecases[i][1]));
		}
		for (int i = 0; i < truecases.length; i++) {
			assertFalse(IdentifyingAnagrams.solution1(falsecases[i][0],
				falsecases[i][1]));
		}
	}

	@Test
	public void testSolution2() {
		String[][] truecases = trueCases();
		String[][] falsecases = falseCases();
		for (int i = 0; i < truecases.length; i++) {
			assertTrue(IdentifyingAnagrams.solution2(truecases[i][0],
				truecases[i][1]));
		}
		for (int i = 0; i < truecases.length; i++) {
			assertFalse(IdentifyingAnagrams.solution2(falsecases[i][0],
				falsecases[i][1]));
		}
	}

}
