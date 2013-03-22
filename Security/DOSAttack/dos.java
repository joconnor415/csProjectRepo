import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
// Denial-of-service attack and countermeasure

/*
 * Write a program to find out how many GETs per second your web server can handle.
 *  This program will take the time between GET requests as input and generate GET 
 *  requests to a certain URL on your web server to overload your web server. Measure
 *   the time it takes for the requested website (HTML, PHP, etc) to be returned, and 
 *   see at what rate (how many GETs per second) the response starts to slow down, and 
 *   at what rate the response time becomes more than 200ms.
 */
public class Client {
	public static long totalTime = 0;
	public static long totalResponseTime = 0;
	String serverWebsite;
	int input=0;
	public static int numThreads=0;
	public static ArrayList <Long> responseTimeArr= new ArrayList <Long>();

	/*
	 * Client Constructor
	 */
	public Client(String website, int input, int numThreads) {
		this.serverWebsite = website;
		this.input=input;
		this.numThreads=numThreads;

		ClientThread[] threads = new ClientThread[numThreads];
		for (int i = 0; i < numThreads; i++) {

			threads[i] = new ClientThread();
			//Thread.sleep(0, input);
			threads[i].run();

		}
		for (int i = 0; i < numThreads; i++) {

			try {
				threads[i].join();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

		}
	}

	private class ClientThread extends Thread implements Runnable {

		public void run() {

			URL myWebsite;
			try {
				// Thread.sleep(100);
				myWebsite = new URL(serverWebsite);
				HttpURLConnection serverConnec = (HttpURLConnection) myWebsite
						.openConnection();
				(serverConnec).setRequestMethod("GET");
				
				long startTime = System.currentTimeMillis();
				serverConnec.connect();
				long endTime = System.currentTimeMillis();
				long duration = endTime - startTime;

				totalTime += duration;

				BufferedReader serverReader = new BufferedReader(
						new InputStreamReader(serverConnec.getInputStream()));

				String readResponse;
				while ((readResponse = serverReader.readLine()) != null) {
					System.out.println(readResponse);
				}
				long endResponseTime = System.currentTimeMillis();
				totalResponseTime += endResponseTime - startTime;

				
				serverReader.close();
			} 
			
			catch (Exception e) {
				e.printStackTrace();
			}

		}

	}

	//Function to calculate the number of gets per second
	public static void getsPerSecond() {
		//convert to seconds
		double total = (double) totalTime / (double) 1000;
		//number of threads per second
		double x = (numThreads/total);
		System.out.println("GETs per sec: " + x);

	}

	public static void averageResponseTime() {

		//convert to seconds
		double total = (double) totalTime / (double) 1000;
		//number of threads per second
		System.out.println(total);
		System.out.println("Avg Response Time: " + (float) totalResponseTime / numThreads);

	}

	public static void main(String[] args) throws Exception {
		new Client(args[0], Integer.valueOf(args[1]), Integer.valueOf(args[2]));
		System.out.println("before" + totalTime);
		getsPerSecond();
		averageResponseTime();
		System.out.println("after" + totalTime);

	}

}
