# test_ramenbowl.py
"""
Tests for RamenBowl module.
"""

import unittest
from ramenbowl import RamenBowl

class TestRamenBowl(unittest.TestCase):
    """Test cases for RamenBowl class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RamenBowl()
        self.assertIsInstance(instance, RamenBowl)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RamenBowl()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
