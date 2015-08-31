package stringReOrdering;

import static org.junit.Assert.*;

import org.junit.Test;

public class ReOrderTest {

	@Test
	public void testHash() {
		String dict = "oleh";
		ReOrder r = new ReOrder(dict);
		assertEquals(r.getPrecedence("l"),new Integer(1));
		assertEquals(r.getPrecedence("e"),new Integer(2));
		assertEquals(r.getPrecedence("w"),new Integer(-1));
	}
	
	@Test
	public void testTranslate1() {
		// Example
		String dict = "oleh";
		String word = "helloworld";
		ReOrder r = new ReOrder(dict);
		String translate = r.translate(word);
		assertEquals("wrdoollleh", translate);
		// Example from site
		word = "hello";
		r = new ReOrder(dict);
		translate = r.translate(word);
		assertEquals("olleh", translate);
		// Trivial case
		dict = "";
		word = "hello";
		r = new ReOrder(dict);
		translate = r.translate(word);
		assertEquals("hello", translate);
		// Test redundancy
		dict = "elleelelelel";
		word = "hello";
		r = new ReOrder(dict);
		translate = r.translate(word);
		assertEquals("hoell", translate);
	}
}
