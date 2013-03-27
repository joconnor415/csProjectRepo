	/**
	 * Author: Jeremiah O'Connor
	 * 
	 * Class: CS 640 Bioinformatics
	 * 
	 * Purpose: Write a generalized Hidden Markov Model that employs the forward algorithm (which is a 
	 * dynamic programming algorithm) for scoring. You may hard-code in a transition matrix, emissions 
	 * matrix and start probabilities. Your program should read in a string of any length composed of the 
	 *	characters {a, c, t, g} and output the score of that string, given the HMM  defined below.
	 *
	 * Note: use MnumOfSymbolsInAlphabet variable to prevent underflow
	 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class HiddenMarkovModel {

	private static final int NnumOfHiddenStates = 3; //N = 3,  hidden states S1, S2,  S3
	private static final int MnumOfSymbolsInAlphabet = 4; //M=4 symbols in alphabet {a, c, t, g}
	
	//Initial probability distribution vector  of length N: π = {π1 …, πN}
	private static double[] pi = { .25, .5, .25 };
	//Emission probability matrix of size N X M where ei(c) probability that state i emits character c
	private static double emissionProbMatrix[][] = { { .4, .4, .1, .1 },
			{ .25, .25, .25, .25 }, { .1, .1, .4, .4 } };
	//Transition probability matrix of size N X N where T ij  is probability of transition from state i to state j
	private static double[][] transProbMatrix = { { .4, .5, .1 },
			{ .1, .4, .5 }, { .3, .3, .4 } };
	
	//test cases
	//private static double[][] transProbMatrix = {{.333333333333333333333333333, .333333333333333333333333333,  .333333333333333333333333333 }, {.333333333333333333333333333, .333333333333333333333333333,  .333333333333333333333333333 }, {.333333333333333333333333333, .333333333333333333333333333,  .333333333333333333333333333}};
	//private static double[][] emissionProbMatrix= {{.25,  .25,  .25,  .25 }, {.25,  .25,  .25,  .25 }, { .25,  .25,  .25,  .25 }};                                   
	//private static double[] testInitProb =  {.333333333333333333333333333, .333333333333333333333333333,  .333333333333333333333333333};

	/**
	 * 
	 * Initialization: a(i) = πiei(O1)
	 * initialize the scoring vector for with the corresponding (0th in main) nucleotide to int in the given sequence
	 * @param scoringMatrix- will pass in the initialized scoring matrix
	 * @param dna string converted to integers
	 * @return- the score of the string
	 */
	public static double[] initScoringMatrix(int initCol) {
		double[] initScoreVector = new double[NnumOfHiddenStates];

		for (int i = 0; i < NnumOfHiddenStates; i++) {
			initScoreVector[i] = (pi[i] * emissionProbMatrix[i][initCol])
					* MnumOfSymbolsInAlphabet;
		}
		return initScoreVector;
	}
	

	/**
	 * 
	 * iterate through the converted dna list, visiting every nucleotide converted to integer
	 * performing the forward algorithm  
	 * @param scoringMatrix- will pass in the initialized scoring vector
	 * @param dna string converted to integers
	 * @return- the probability of the given sequence
	 */
	public static double[] iterThruConvDNAList(double[] scoringMatrix,
			ArrayList<Integer> dna) {
		int i = 1;
		while (i < dna.size()) {
			scoringMatrix = forwardAlgorithm(scoringMatrix, dna.get(i));
			i++;
		}
		return scoringMatrix;
	}

	/**
	 * 
	 * HMM forward algorithm- example of dynamic programming
	 * calculates probability of given sequence, and builds forward table.
	 * uses all the data members in the algorithm
	 * @param scoringMatrix- will pass in the originally initialized/next scoring vector
	 * @param dnaIndex- the converted nucleotide integer at index i in the converted dna string
	 * @return- the probability of the given sequence up until the specific index
	 */
	public static double[] forwardAlgorithm(double[] scoringMatrix, int dnaIndex) {

		double[] nextProbSet = new double[NnumOfHiddenStates];
		for (int i = 0; i < NnumOfHiddenStates; i++) {
			for (int j = 0; j < NnumOfHiddenStates; j++) {
				nextProbSet[i] += transProbMatrix[j][i] * scoringMatrix[j];
			}
			nextProbSet[i] *= emissionProbMatrix[i][dnaIndex]
					* MnumOfSymbolsInAlphabet;

		}
		return nextProbSet;
	}
	
	/**
	 * 
	 * converts DNA nucleotide string to integers; a,c,t,g --> 0,1,2,3
	 * @param dnaString- string of dna nucleotide sequence a,c,t,g
	 * 
	 * @return- dna nucleotide sequence converted to integers
	 */
	public static ArrayList<Integer> convertDNA2IntArray(String dnaString) {
		ArrayList<Integer> nucleotide2IntegerArray = new ArrayList<Integer>();

		for (int i = 0; i < dnaString.length(); i++) {
			if (dnaString.substring(i, i + 1).equals("a")) {
				nucleotide2IntegerArray.add(0);
			} else if (dnaString.substring(i, i + 1).equals("c")) {
				nucleotide2IntegerArray.add(1);
			} else if (dnaString.substring(i, i + 1).equals("t")) {
				nucleotide2IntegerArray.add(2);
			} else if (dnaString.substring(i, i + 1).equals("g")) {
				nucleotide2IntegerArray.add(3);
			} else {

			}
		}
		return nucleotide2IntegerArray;

	}

	/**
	 * 
	 * read in a string of any length composed of the characters {a, c, t, g} 
	 * use regex expression to remove whitespace and trailing newlines
	 * @param dnaFile- takes in a dna file, nucleotide sequence a,c,t,g
	 * 
	 * @return- dna nucleotide sequence as string
	 */
	public static String readFile(String dnaFile) throws IOException {

		FileReader fr = new FileReader(dnaFile);
		BufferedReader br = new BufferedReader(fr);
		String s = "";
		String dnaString = "";
		while ((s = br.readLine()) != null) {
			dnaString += s.trim().replaceAll("(?m)^[ \t]*\r?\n", "");

		}
		fr.close();
		return dnaString;
	}
	//main
	public static void main(String[] args) throws Exception {

		String mysteryGene = HiddenMarkovModel.readFile(args[0]);
		ArrayList<Integer> convertedGeneArray = HiddenMarkovModel
				.convertDNA2IntArray(mysteryGene);

		int initElemInDNA = convertedGeneArray.get(0);
		double[] initializedScoringMatrix = (HiddenMarkovModel
				.initScoringMatrix(initElemInDNA));
		//test cases
		//double[] initializedScoringMatrix={.333333333333333333333333333, .333333333333333333333333333,  .333333333333333333333333333};
		double[] totalScoringMatrix = HiddenMarkovModel.iterThruConvDNAList(
				initializedScoringMatrix, convertedGeneArray);

		for (int i = 0; i < totalScoringMatrix.length; i++) {
			System.out.println("S" + (i+1) + ": " + totalScoringMatrix[i]);
		}
		double total=0;
		for (int i = 0; i < totalScoringMatrix.length; i++) {
			total+= totalScoringMatrix[i];
			
		}
		System.out.println("Total: " + total);

	}

}
