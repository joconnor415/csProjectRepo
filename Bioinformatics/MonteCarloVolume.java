import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.LineNumberReader;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class MCPart1 {
	private static double s = 0;
	private static double s2 = 0;
	private static int numOfAtoms = 0;
//	private static double f = 0;
//	private static double f2 = 0;

	// list of lists
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

	// box dimensions
	private static double boxLength = 0;
	private static double boxWidth = 0;
	private static double boxHeight = 0;

	public static double generateRandDouble(double min, double max) {
		// Random r = new Random();
		double randDouble = min + (max - min) * Math.random();
		return randDouble;

	}


	public static double distForm3d(double x1, double x2, double y1, double y2,
			double z1, double z2) {

		double distance = Math.sqrt(((x2 - x1) * (x2 - x1))
				+ ((y2 - y1) * (y2 - y1)) + ((z2 - z1) * (z2 - z1)));
		return distance;
	}

	public static double calcVolumeBox(double l, double w, double h) {
		double volume = l * w * h;
		return volume;
	}

	public static double findMax(ArrayList<Double> arr, ArrayList<Double> r) {
		double arrMax = arr.get(0);
		for (int i = 0; i < arr.size(); i++) {
			// System.out.println(r.get(i));
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

	public static void integral(ArrayList<Double> x, ArrayList<Double> y,
			ArrayList<Double> z, ArrayList<Double> r) {
		Random rand = new Random();
		int min = 0;
	
		int max = 1000;
		int randomNum = rand.nextInt(max - min + 1) + min;
		// Random r1= new Random();
		// int randomNum = r1.nextInt();
		//run int at 10, 100, 1000, 10000 not random
		System.out.println("Random " + randomNum);
		for (int k = 0; k < 100000; k++) {
			double randX = (generateRandDouble(xMin, xMax));
			double randY = (generateRandDouble(yMin, yMax));
			double randZ = (generateRandDouble(zMin, zMax));

			int fx = 0;
			for (int i = 0; i < numOfAtoms; i++) {

				double distance = (distForm3d(randX, x.get(i), randY, y.get(i),
						randZ, z.get(i)));

				if (distance <= r.get(i)) {

					fx = 1;
					break;
				}
			}
			s += fx;
			s2 += fx * fx;

		}

		System.out.println("s= " + s);
		System.out.println("s2= " + s2);
	}


	/**
	 * 
	 * read in a string of any length composed of the characters {a, c, t, g}
	 * use regex expression to remove whitespace and trailing newlines
	 * 
	 * @param fileName
	 *            - takes in a file, coordinates x,y,z and radius r
	 * 
	 * 
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




		integral(xArray, yArray, zArray, radiusArray);

		double f = s / 100000;
		double f2 = s2 / 100000;

		System.out.println("Standard Deviation: " + calcVolumeBox(boxLength, boxWidth, boxHeight) * (Math.sqrt((f2 - f * f) / 100000)));
		Double newVol = f * calcVolumeBox(boxLength, boxWidth, boxHeight);
		System.out.println("Volume: " + newVol);

	}
}
