package stringReOrdering;

public class StringReordering {

	public static void main(String[] args) {
		String dict = args[0];
		String word = args[1];
		
		ReOrder r = new ReOrder(dict);
		String translate = r.translate(word);
		
		System.out.println("Dict is: " + dict);
		System.out.println("Word is: " + word);
		System.out.println("Translation is: " + translate);
	}

}