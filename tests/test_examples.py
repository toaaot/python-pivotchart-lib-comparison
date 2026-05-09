"""
Unit tests for the pivot chart comparison examples.

This module contains basic tests to verify that all examples work correctly.
"""

import unittest
import os
import sys
import pandas as pd

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
            'sample_data.csv'
        )
    
    def test_sample_data_exists(self):
        """Test that sample data file exists."""
        self.assertTrue(os.path.exists(self.data_path), "sample_data.csv not found")
    
    def test_sample_data_loads(self):
        """Test that sample data can be loaded as DataFrame."""
        df = pd.read_csv(self.data_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
    
    def test_sample_data_columns(self):
        """Test that sample data has expected columns."""
        df = pd.read_csv(self.data_path)
        expected_columns = {'date', 'product', 'region', 'sales', 'quantity', 'profit'}
        self.assertEqual(set(df.columns), expected_columns)
    
    def test_sample_data_no_null_values(self):
        """Test that sample data has no null values."""
        df = pd.read_csv(self.data_path)
        self.assertEqual(df.isnull().sum().sum(), 0)


class TestPandasFunctionality(unittest.TestCase):
    """Test pandas pivot table functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        data_path = os.path.join(
            os.path.dirname(__file__), 
            '..', 
            'data', 
            'sample_data.csv'
        )
        self.df = pd.read_csv(data_path)
    
    def test_pivot_table_creation(self):
        """Test that pivot tables can be created."""
        pivot = pd.pivot_table(
            self.df,
            values='sales',
            index='product',
            columns='region',
            aggfunc='sum'
        )
        self.assertIsNotNone(pivot)
        self.assertGreater(len(pivot), 0)
    
    def test_groupby_aggregation(self):
        """Test that groupby aggregation works."""
        result = self.df.groupby('region')['sales'].sum()
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)


if __name__ == '__main__':
    unittest.main()
