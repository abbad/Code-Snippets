from merge_sort import merge_sort
from unittest import TestCase, main
import random
class TestStringCompression(TestCase):
	
	def test_merge_sort_empty_array(self):
		""" 
			Test merge sort function with an empty string. 
		"""
		self.assertEqual(merge_sort([]), [])
		
	def test_merge_sort_already_sorted_array(self):
		"""	
			Test merge sort function when sending an already sorted array. 
		"""
		self.assertEqual(merge_sort([1,2,3]), [1,2,3])
		
	def test_merge_sort_one_element(self):
		"""	
			Test merge function when sending an array of one element. 
		"""
		self.assertEqual(merge_sort([1]), [1])
		
	def test_merge_sort_one_reversed(self):
		"""
			Test merge function when sending reveresed input.
		"""
		self.assertEqual(merge_sort([3,2,1]), [1,2,3])
	
	def test_merge_sort_random(self):
		"""
			Test function when giving it an array of random strings.
		"""
		random_integers =[int(1000*random.random()) for i in xrange(200)]
		self.assertEqual(merge_sort(random_integers), sorted(random_integers))
										
		
if __name__ == '__main__':
    main()
