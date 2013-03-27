import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.LineNumberReader;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;


public class MCPart2 {

	private static int numOfAtoms = 0;
	
	private static ArrayList<Double> xArray = new ArrayList<Double>();
	private static ArrayList<Double> yArray = new ArrayList<Double>();
	private static ArrayList<Double> zArray = new ArrayList<Double>();
	private static ArrayList<Double> radiusArray = new ArrayList<Double>();

	private static double xMin = 0;
	private static double xMax = 0;
	private static double yMin = 0;
	private static double yMax = 0;
	private static double zMin = 0;
	private static double zMax = 0;
//	private static double f=0;
//	private static double f2=0;

	// box dimensions
	private static double boxLength = 0;
	private static double boxWidth = 0;
	private static double boxHeight = 0;
	//private static double ballSurface = 0;


	public static double generateRandDouble(double min, double max) {
		Random r = new Random();
		double randDouble = min + (max - min) * r.nextDouble();
		return randDouble;

	}

	public static double distForm3d(double x1, double x2, double y1, double y2,
			double z1, double z2) {

		double distance = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1)
				* (y2 - y1) + (z2 - z1) * (z2 - z1));
		return distance;
	}

	public static double calcSurfaceArea(Double r) {
		double SR = 4 * Math.PI * (r * r);
		return SR;
	}

	public static double calcVolumeBox(double l, double w, double h) {
		double volume = l * w * h;
		return volume;
	}

	public static double findMax(ArrayList<Double> arr, ArrayList<Double> r) {
		double arrMax = arr.get(0);
		for (int i = 0; i < arr.size(); i++) {
	
			if (arr.get(i) + r.get(i) > arrMax) {
				arrMax = arr.get(i) + r.get(i);
			}
		}
		return arrMax;
	}

	public static double findMin(ArrayList<Double> arr, ArrayList<Double> r) {
		double arrMin = arr.get(0);
		for (int i = 1; i < arr.size(); i++) {
			if (arr.get(i) - r.get(i) < arrMin) {
				arrMin = arr.get(i) - r.get(i);
			}
		}
		return arrMin;
	}

	public static void integral(ArrayList<Double> x, ArrayList<Double> y, ArrayList<Double> z,
			ArrayList<Double> r) {

		double totalMean1 = 0;
		double totalMean2 = 0;
		double surface= 0.0;
//		ballSurface += calcSurfaceArea(r.get(k));// gets radius of that
		double ballSurface = 0.0;
		// double ballSurface=0;
		for (int k = 0; k < numOfAtoms; k++) { //NC= 2775
		
			

			double rho = r.get(k);
			double center1 = x.get(k);
			double center2 = y.get(k);
			double center3 = z.get(k);

			double s=0;
			double s2=0;

//			Random rand = new Random();
//			int min = 0;
//			// 1000 just for testing purposes
//			int max = 1000;
//			int randomNum = rand.nextInt(max - min + 1) + min;
			//can plug random number between whatever two values in
			for (int i = 0; i < 10000; i++) {

				double phi = generateRandDouble(0, Math.PI);
				double theta = generateRandDouble(0, 2 * Math.PI);
				
//				double xcoord = rho * Math.sin(phi) * Math.sin(theta) + center1;
//				double ycoord = rho * Math.sin(phi) * Math.cos(theta) + center2;
				double xcoord = rho * Math.sin(phi) * Math.cos(theta) + center1;
				double ycoord = rho * Math.sin(phi) * Math.sin(theta) + center2;
				double zcoord = rho * Math.cos(phi) + center3;

				int fx = 1;

				for (int j = 0; j < numOfAtoms; j++)
				{
					double distance = (distForm3d(xcoord, x.get(j), ycoord, y.get(j), zcoord, z.get(j)));
					
					if (distance <=  r.get(j) && (j!=k)) 
					{ 
							fx=0;
							break;
					}	
				}
				s +=  fx;
				s2 += fx * fx;

			}
			double f = s / 10000.0;
			double f2= s2/10000.0;
			totalMean1+=f;
			totalMean2+=f2;

			ballSurface += calcSurfaceArea(r.get(k));
			double newSurface= calcSurfaceArea(r.get(k)) *f;
			
//			System.out.println("New Surface" + newSurface);
			surface+=newSurface;
//			System.out. println("Surface: " + surface);

		}
		System.out. println("Surface: " + surface);
		double totalN= 10000 * numOfAtoms;
		totalMean1= totalMean1/totalN;
		totalMean2= totalMean2/totalN;
		
		double percError= (Math.abs(surface- 36764.21)/ 36764.21) *100;
		System.out.println("Percentage Error: "+ percError);
		System.out.println("Standard Deviation: " + ballSurface * (Math.sqrt((totalMean2 - (totalMean1 * totalMean1)) / (totalN))));
		
	}

	
	/**
	 * 
	 * @param fileName
	 *            - takes in a file, coordinates x,y,z and radius r
	 */
	public static void readFile(String fileName) {
		try {
			File file = new File(fileName);
			Scanner scanner = new Scanner(file);
			scanner.nextLine();
			while (scanner.hasNext()) {
				int counter = 0;
				if (counter == 0) {
					xArray.add(scanner.nextDouble());
					counter++;
				}
				if (counter == 1) {
					yArray.add(scanner.nextDouble());
					counter++;
				}
				if (counter == 2) {
					zArray.add(scanner.nextDouble());
					counter++;
				}
				if (counter == 3) {
					radiusArray.add(scanner.nextDouble());
					counter++;
				}

				if (counter == 4) {
					counter = 0;
				}
			}
			scanner.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	public static double mean(double s, double n) {
		return s / n;
	}

	public static double surfaceArea(double l, double w, double h) {
		double rSurfArea = 0;
		rSurfArea = 2 * (l * w + l * h + w * h);
		return rSurfArea;
	}

	public static String readfirstLineOfFile(String dnaFile) throws IOException {

		FileReader fr = new FileReader(dnaFile);
		LineNumberReader ln = new LineNumberReader(fr);

		String s = "";
		while (ln.getLineNumber() == 0) {
			s = ln.readLine().trim().replaceAll("(?m)^[ \t]*\r?\n", "");
		}
		return s;
	}

	public static void main(String[] args) throws Exception {

		String x = readfirstLineOfFile(args[0]);
		numOfAtoms = Integer.parseInt(x);

		readFile(args[0]);
		xMin = findMin(xArray, radiusArray);
		xMax = findMax(xArray, radiusArray);
		yMin = findMin(yArray, radiusArray);
		yMax = findMax(yArray, radiusArray);
		zMin = findMin(zArray, radiusArray);
		zMax = findMax(zArray, radiusArray);

		boxLength = (xMax - xMin);
		boxWidth = (yMax - yMin);
		boxHeight = (zMax - zMin);

		integral(xArray,yArray, zArray, radiusArray);


	}
}
