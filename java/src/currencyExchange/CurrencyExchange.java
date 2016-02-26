package currencyExchange;

import java.io.BufferedReader;
//import java.io.IOException;
import java.io.InputStreamReader;

/** A solution to post on 
 * http://programmingpraxis.com/2015/02/27/currency-exchange/
 * 
 * @author amomin
 *
 */
public class CurrencyExchange {

	public static void main(String[] args) {
		String from = "EUR";
		String to = "GBP";
		double amt = 130000;
		double rate;
	
		BufferedReader br = new BufferedReader(
			new InputStreamReader(System.in));

		try {
			System.out.println("Enter the source currency");
			from = br.readLine();
			System.out.println("Enter the destination currency");
			to = br.readLine();
			System.out.println("Enter the source amount");
			amt = Double.parseDouble(br.readLine());
			ExchangeRate ex = new ExchangeRate();
			ex.setFrom(from);
			ex.setTo(to);
			ex.updateExchangeRate();
			rate =  ex.getExchangeRate();
			System.out.printf("Exch rate from %s to %s is %.4f %n", from, to, rate);
			System.out.printf("Amount in %s is %.2f %n", from, amt);
			System.out.printf("Amount in %s is %.2f %n", to, amt*rate);
		} catch (Exception e) {
			System.out.printf("Exception caught with message: %s %n%n", e.getMessage());
		}
	}
}