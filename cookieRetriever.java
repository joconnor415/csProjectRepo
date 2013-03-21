import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class CookieRetriever{

	private ArrayList<String> cookies;

	public CookieRetriever (String path){

		cookies= new ArrayList<String>();
		retrieveCookie(path);
	}

	public void retrieveCookie(String path){

		try{
			BufferedReader br= new BufferedReader (new FileReader(path));
			String line = new String();

			while ((line= br.readLine()) != null){
				if (line.startsWith("Cookie:")){
					String idCookie = line.split(":")[1].trim();
					if (!cookie.contains(idCookie)){
						cookies.add(idCookie)
					}
				}
			}
			br.close();
		} catch (Exception e){
			e.printStackTrace();
		}

	}
	public ArrayList<String> getCookie()
	{
		return cookies;
	}

}