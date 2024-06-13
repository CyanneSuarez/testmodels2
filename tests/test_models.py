import unittest
from testmodels2.models import Product  # Adjust the import to your project's structure
from testmodels2 import db

class TestProductModel(unittest.TestCase):

    def setUp(self):
        # Set up a test database or any required initial state
        db.create_all()  # Ensure the database and tables are created
        self.product = Product(name="Test Product", description="This is a test product", price=9.99, stock=10)
        db.session.add(self.product)
        db.session.commit()

    def tearDown(self):
        # Clean up the database after each test
        db.session.remove()
        db.drop_all()

    def test_update_product(self):
        # Update the product in the database
        product = Product.query.filter_by(name="Test Product").first()
        self.assertIsNotNone(product)

        product.name = "Updated Test Product"
        product.price = 19.99
        db.session.commit()

        # Verify the update
        updated_product = Product.query.filter_by(name="Updated Test Product").first()
        self.assertIsNotNone(updated_product)
        self.assertEqual(updated_product.name, "Updated Test Product")
        self.assertEqual(updated_product.price, 19.99)

if __name__ == "__main__":
    unittest.main()
