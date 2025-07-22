#James Barnson
#10/9/2023
#CSE107
#Lab1 Code file

# The purpose of this code is to execute instructions for running a probability experiment.It corresponds to lab 1 at https://people.ucsc.edu/~ptantalo/cse107/Fall23/lab1.pdf

import numpy as np
import random as rand
import tabulate as tab

def coinFlip(weight):       
	x = rand.randrange(10)/10
	flip = 0
	if x < weight:	
		flip = 0
	elif x >= weight: flip = 1
	return flip

def experiment(n, weight):
	alice = 0 #initialize to count number of Alice's heads
	bob = 0 #initialize to count number of Bob's heads
	
	prob = weight
	i = 0
	while i < n: #perform n flips for alice
		y = coinFlip(prob)
		alice = alice + y #add the result to the counter
		i += 1
	
	
	i = 0
	while i <= n: #perform n+1 flips for bob
		y = coinFlip(prob)
		bob = bob + y
		i += 1

	
	if bob > alice: return 1
	else: return 0	


def relativeFrequency(r, n, weight): 
#find relative frequency. args r: repetitions, n: number of flips, weight: probability weight
	bobWins = 0 #variable to store how often Bob wins
	
	prob = weight	
	j = 0
	while j < r:
		w = experiment(n, prob)
		bobWins = bobWins + w
		j += 1
	
	relFreq = bobWins/r #calculate the relative frequency of Bob winning
#	print("Bob won ", relFreq*100, " % of the time.")
	return relFreq
	

def Main():
	#Generate a table of relative frequencies based on probabilities.
	fairProb = 0.5 # First experiment's probability
	probList = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

	fairFlip = relativeFrequency(1000, 100, 0.5)
	print("The relative frequency of Bob winning with a fair coin is", f"{fairFlip:.4f}", ".")

	weightPt2 = relativeFrequency(1000, 100, 0.2)
	weightPt3 = relativeFrequency(1000, 100, 0.3)
	weightPt4 = relativeFrequency(1000, 100, 0.4)
	weightPt5 = relativeFrequency(1000, 100, 0.5)
	weightPt6 = relativeFrequency(1000, 100, 0.6)
	weightPt7 = relativeFrequency(1000, 100, 0.7)
	weightPt8 = relativeFrequency(1000, 100, 0.8)

	data = [[0.2, weightPt2],
		[0.3, weightPt3],
		[0.4, weightPt4],
		[0.5, weightPt5],
		[0.6, weightPt6],
		[0.7, weightPt7],
		[0.8, weightPt8]]

	col_names = ["p", "relative frequency"]

	print(tab.tabulate(data, headers=col_names, floatfmt=(".1f", ".4f")))	

Main()
