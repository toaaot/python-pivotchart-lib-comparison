"""
Unit tests for the pivot chart comparison examples.

This module contains basic tests to verify that all examples work correctly.
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

# expected_columns = { "SessionName", "Player", "Character", "ActionType", "TargetNum", "RollDate", "RollTime", "RollOutcome" }

class TestPandasFunctionality(unittest.TestCase):
    """Test pandas pivot table functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        data_path = os.path.join(
            os.path.dirname(__file__), 
            '..', 
            'data', 
            'game_sessions.csv'
        )
        self.df = pd.read_csv(data_path)
    
    def test_pivot_table_creation(self):
        """Test that pivot tables can be created."""
        pivot = pd.pivot_table(
            self.df,
            values='Player',
            index='RollDate',
            columns='RollOutcome',
            aggfunc='value_counts'
        )
        LOGGER.info("\r\npivot table:\r\n" + str(pivot))
        self.assertIsNotNone(pivot)
        self.assertGreater(len(pivot), 0)
    
    def test_groupby_aggregation(self):
        """Test that groupby aggregation works."""
        result = self.df.groupby('Player')['RollOutcome'].value_counts()
        LOGGER.info("\r\naggregation result:\r\n" + str(result))
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)


if __name__ == '__main__':
    unittest.main()

# end of file
