# coding: UTF-8

'''
	Ternary search is similar to linear and binary search that is used to determine the position of an element in a list. 
	In binary search, the sorted array is divided into two parts while in ternary search the sorted array is divided into three
	parts. 

	It is a divide and conquer algorithm where in each iteration, it neglects 2/3 of the part and repeats the same operation with 
	the remaining 1/3.
'''

def ternary_search(left, right, key, array):

	if (left <= right):
		midl = left + (right - left) / 3
		midr = right - (right - left) / 3

		if array[midl] == key:
			return midl

		if array[midr] == key:
			return midr

		if array[midl] > key:
			return ternary_search(left, midl-1, key, array)

		if array[midr] < key:
			return ternary_search(midr+1, right, key, array)

		else:
			return ternary_search(midl+1, midr-1, key, array)

	return -1

# Writing unit-test for the above function
import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		self.array = [2, 5, 6, 12, 17, 23, 34, 45, 67, 81]
		self.right = len(self.array)
		self.key = 23

	def test(self):
		self.assertEqual(ternary_search(0, self.right, self.key, self.array), 5)

if __name__ == "__main__":
	unittest.main()
