# test Shopping Cart
from cart import ShoppingCart

from product import Product

import unittest

class ShoppingCartTestCase(unittest.TestCase):
    def test_add_and_remove_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        cart.remove_product(product)

        self.assertDictEqual({}, cart.products)
    
    def test_add_two_products(self):
        cart = ShoppingCart()
        product1 = Product('shoes', 'S', 'blue')
        product2 = Product('tshirt', 'M', 'black')

        cart.add_product(product1)
        cart.add_product(product2)

        expected_cart_value = {'SHOES-S-BLUE':{'quantity': 1}, 'TSHIRT-M-BLACK':{'quantity':1}}
        self.assertDictEqual(expected_cart_value, cart.products)
    
    def test_remove_product_from_empty_cart(self):
        cart = ShoppingCart()
        product1 = Product('shoes', 'S', 'blue')
        cart.remove_product(product1)
        
        self.assertDictEqual({}, cart.products)