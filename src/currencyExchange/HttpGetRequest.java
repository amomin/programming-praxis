package currencyExchange;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpGetRequest {

	private String urlstring;
	private String httpResponse;
	
	private final String USER_AGENT = "Mozilla/5.0";
	
	public void setUrl(String u) {
		urlstring = u;
	}
	
	public void execute() throws Exception {
		URL url = new URL(urlstring);
		HttpURLConnection con = 
				(HttpURLConnection) url.openConnection();
		con.setRequestMethod("GET");
		con.setRequestProperty("User-Agent", USER_AGENT);
		
		int responseCode = con.getResponseCode();
		
		BufferedReader in = new BufferedReader(
			new InputStreamReader(con.getInputStream()));
		
		String inputLine;
		StringBuffer response = new StringBuffer();
		
		while ((inputLine = in.readLine()) != null) {
			response.append(inputLine);
		}
		in.close();
		httpResponse = response.toString();
	}
	
	public String response() {
		return httpResponse;
	}
}
