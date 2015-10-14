from compress_string import compress_string
from unittest import TestCase, main

class TestStringCompression(TestCase):
	
	def test_empty_string(self):
		""" 
			Test compression function when sending an empty string. 
		"""
		self.assertEqual(compress_string(""), "")
		
	def test_full_string_compression(self):
		"""	
			Test compression function when sending a string that can be fully compressed.
		"""
		self.assertEqual(compress_string("bbccddd"), "b2c2d3")
		
	def test_no_repetitions_compression(self):
		"""	
			Test compression function when sending a string that can be fully compressed.
		"""
		self.assertEqual(compress_string("bccdd"), "bc2d2")
		
	def test_one_character_compression(self):
		"""
			Test compression function when sending a one character string to it. 
		"""
		self.assertEqual(compress_string("bbbb"), "b4")
	
	def test_random_combination(self):
		"""
			Test compression function when sending a random combination. 
		"""
		self.assertEqual(compress_string("hhhhhssvvxvvabbcoo"), "h5s2v2xv2ab2co2")
										
		
if __name__ == '__main__':
    main()


