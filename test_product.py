#product tests

import unittest

from product import Product

class ProductTestCase(unittest.TestCase):
    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'SHOES'

        actual_value = small_black_shoes.transform_name_for_sku()

        self.assertEqual(expected_value, actual_value)
    
    def test_transform_color_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'BLACK'

        actual_value = small_black_shoes.transform_color_for_sku()

        self.assertEqual(expected_value, actual_value)
    
    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'SHOES-S-BLACK'

        actual_value = small_black_shoes.generate_sku()

        self.assertEqual(expected_value, actual_value)