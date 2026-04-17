# test_arbitragebot.py
"""
Tests for ArbitrageBot module.
"""

import unittest
from arbitragebot import ArbitrageBot

class TestArbitrageBot(unittest.TestCase):
    """Test cases for ArbitrageBot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArbitrageBot()
        self.assertIsInstance(instance, ArbitrageBot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArbitrageBot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
