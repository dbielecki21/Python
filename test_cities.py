import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
	#tests for 'city_functions.py'

	def test_city_country(self):
		santiago_chile = city_country('santiago', 'chile')
		self.assertEqual(santiago_chile, 'Santiago, Chile')

	def test_city_country_population(self):
		santiago_chile = city_country('santiago', 'chile', population=500000)
		self.assertEqual(santiago_chile, 'Santiago, Chile - population500000')

unittest.main()
