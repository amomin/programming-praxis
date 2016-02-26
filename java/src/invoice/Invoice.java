package invoice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Invoice {

	/** Added basic error handling
	 * 
	 * @param args
	 */
	public static void main(String[] args) {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = "";
		ArrayList<InvoiceLine> invoice = new ArrayList<InvoiceLine>();
		InvoiceLine line = new InvoiceLine();
		int phase = 0;
		while(!input.equals("q")) {
			if (phase % 4 == 0) {
				System.out.printf("Enter next item (type q to quit): ");
				line = new InvoiceLine();
			}
			else if (phase % 4 == 1) {
				line.setName(input);
				System.out.printf("Enter quantity (type q to quit): ");				
			}
			else if (phase % 4 == 2) {
				try {
					line.setQuantity(Integer.parseInt(input));					
				} catch(Exception e) {
					System.out.println("Error parsing line, terminating");
					line = null;
					break;
				}
				System.out.printf("Enter price (type q to quit): ");				
			}
			else if (phase % 4 == 3) {
				try {
					line.setPrice(Float.parseFloat(input));
				} catch(Exception e) {
					System.out.println("Error parsing line, terminating");
					line = null;
					break;
				}
				invoice.add(line);
				System.out.printf("Type to continue, or q to quit: ");	
			}
			try {
				input = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			phase++;
		}
		int lineNum = 0;
		float subTotal = 0;
		float total = 0;
		float taxRate = (float) 0.0525;
		float tax = 0;
		System.out.printf("%10s%20s\n", "", "Praxis Grocery Store");
		Date today = new Date();
		//DateFormat df = DateFormat.getDateInstance(DateFormat.MEDIUM);
		SimpleDateFormat df = new SimpleDateFormat("d MMM yyyy");
		System.out.printf("%10s%20s\n", "", df.format(today));
		for(InvoiceLine l : invoice) {
			lineNum++;
			subTotal += l.total();
			System.out.printf("%-5d %s\n", lineNum, l.toString());
		}
		System.out.printf("%6s%-20s\n", "", "-----");
		System.out.printf("%6s%-20s %23s %.2f\n", "", "Subtotal","",subTotal);
		tax = taxRate * subTotal;
		System.out.printf("%6s%-20s %23s %.2f\n", "", "Tax 5.25%","",tax);
		total = subTotal + tax;
		System.out.printf("%6s%-20s %23s %.2f\n", "", "Total","",total);
		System.out.println("Done");
	}

}
