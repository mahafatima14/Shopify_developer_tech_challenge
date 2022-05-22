"""test suite for the server"""

from flask import Flask

import server
import os
import unittest
from model import connect_to_db, db
from test_data import example_data



class MyAppIntegrationTestCase(unittest.TestCase):
    """Integration tests: testing Flask server."""

    def setUp(self):
        """Stuff to do before every test."""

        print("(setUp ran)")
        # Get the Flask test client
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
        server.app.config["SECRET_KEY"] = "key"
        os.system("dropdb testdb --if-exists")
        os.system("createdb testdb")

        # Connect to test database
        connect_to_db(server.app, "postgresql:///testdb") 

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

        print("(tearDown ran)")
        return

    #testing a GET request route
    def test_index(self):
        """Test the homepage"""
        result = self.client.get('/')
        self.assertEqual(200, result.status_code)
        self.assertIn(b'<h3>Active Inventory</h3>', result.data)

if __name__ == '__main__':
    unittest.main()
