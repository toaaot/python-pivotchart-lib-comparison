"""
Unit tests for the pivot chart comparison examples.

This module contains basic tests to verify that the data loader works correctly.
"""

import unittest
import logging
import os
import sys
import pandas as pd

# see https://stackoverflow.com/questions/4673373/logging-within-pytest-tests
LOGGER = logging.getLogger(__name__)

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestDataLoading(unittest.TestCase):
    """Test that sample data can be loaded correctly."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.data_path = os.path.join(
            os.path.dirname(__file__), 
            '..', 
            'data', 
            'game_sessions.csv'
        )
        self.expected_columns = { "SessionName", "Player", "Character", "ActionType", "TargetNum", "RollDate", "RollTime", "RollOutcome" }
    
    def test_sample_data_exists(self):
        """Test that sample data file exists."""
        LOGGER.info("\r\ndata path:\r\n" + self.data_path)
        self.assertTrue(os.path.exists(self.data_path), "csv data file not found")
    
    def test_sample_data_loads(self):
        """Test that sample data can be loaded as pandas DataFrame."""
        df = pd.read_csv(self.data_path)
        self.assertIsInstance(df, pd.DataFrame)
        LOGGER.info("\r\ndf len:\r\n" + str(len(df)))
        self.assertGreater(len(df), 0)
    
    def test_sample_data_columns(self):
        """Test that sample data has expected columns."""
        df = pd.read_csv(self.data_path)
        LOGGER.info("\r\nexpected columns:\r\n" + str(self.expected_columns))
        self.assertEqual(set(df.columns), self.expected_columns)
    
    def test_sample_data_no_null_values(self):
        """Test that sample data has no null values."""
        df = pd.read_csv(self.data_path)
        self.assertEqual(df.isnull().sum().sum(), 0)


if __name__ == '__main__':
    unittest.main()

# end of file
