package currencyExchange;

/** Uses Bloomberg to compute
 * exchange rates.
 * 
 * TODO: validate input (at least a little)
 * TODO: asynchronize this to fetch the exchange rate
 * in the background.
 * 
 * @author amomin
 *
 */
public class ExchangeRate {

	private String from;
	private String to;
	private double rate;
	private double amount;

	public ExchangeRate() {
		this.from = null;
		this.to = null;
		this.amount = -1;
		this.rate = -1;
	}
	public void setFrom(String from) {
		this.from = from;
	}
	public void setTo(String to) {
		this.to = to;
	}
	public void setAmount(double amount) {
		this.amount = amount;
	}
	
	public double getExchangeRate() 
			throws java.lang.NullPointerException {
		if (rate == -1) {
			throw new java.lang.NullPointerException("Rate not set");
		}
		return rate;
	}
	
	public double getToAmount() throws Exception {
		if (rate == -1) {
			throw new java.lang.NullPointerException("Rate not set");
		}
		if (amount == -1) {
			throw new java.lang.NullPointerException("Amount not set");
		}
		return this.rate * this.amount;
	}
	
	public void updateExchangeRate() throws Exception {
		if (this.from == null || this.to == null) {
			throw new java.lang.NullPointerException("Must set exchange currencies");
		}
		String url = String.format("https://www.bloomberg.com/quote/%s%s:CUR", 
			from, to);
		HttpGetRequest req = new HttpGetRequest();
		req.setUrl(url);
		req.execute(); // throws HTTP exception
		String res = req.response();
		String srate = (res.replaceAll(".*<span class=\" price\">\\s*([0-9\\.]+)?.*", 
				"$1"));
		try {
			this.rate = Double.parseDouble(srate);
		} catch (NumberFormatException e) {
			throw new 
				java.lang.NumberFormatException("Error parsing exchange rate " + 
				" from HTTP Result");
		}
	}
}
