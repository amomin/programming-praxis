package stringReOrdering;

import java.util.HashMap;

public class ReOrder {

	private String dict;
	private int n;
	private HashMap<String, Integer> hm;
	
	public ReOrder(String d) {
		this.dict = d;
		hm = new HashMap<String, Integer>();
		this.n = 0;
		for (int i = 0; i < d.length(); i++) {
			String c = String.valueOf(d.charAt(i));
			if (!hm.containsKey(c)) {
				hm.put(c, i);
				n = i;
			}
		}
	}

	protected Integer getPrecedence(String s) {
		if (hm.containsKey(s)) {
			return hm.get(s);
		} else {
			return -1;
		}
	}
	
	public String translate(String w) {
		StringBuilder prefix = new StringBuilder();
		int[] counter = new int[this.n + 1];
		for (int i = 0; i < counter.length; i++) {
			counter[i] = 0;
		}
		for (int i = 0; i < w.length(); i++) {
			String c = String.valueOf(w.charAt(i));
			if (hm.containsKey(c)) {
				counter[hm.get(c)]++;
			} else {
				prefix.append(c);
			}
		}
		for (int i = 0; i < counter.length; i++) {
			if (counter[i] > 0) {
				for (int j = 0; j < counter[i]; j++) {
					prefix.append(dict.charAt(i));
				}
			}
		}
		return prefix.toString();
	}
}
