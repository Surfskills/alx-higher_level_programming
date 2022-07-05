#!/usr/bin/python3
"""Python 3 code for Pascal's Triangle
A simple O(n^3) program for Pascal's Triangle
Function to print first n lines of Pascal's Triangle"""

def pascal_triangle(n):

"""Iterate through every line and print entries in it"""
	for line in range(0, n) :
	
"""Every line has number of integers equal to line number"""	
		for i in range(0, line + 1) :
			print(binomialCoeff(line, i)," ", end = "")
		print()
		
