"""Data loader for RPG game session data."""
import pandas as pd
import os
from pathlib import Path

def load_game_sessions(filepath=None):
    """
    Load RPG game session data from CSV file.
    
    Args:
        filepath (str, optional): Path to CSV file. Defaults to data/game_sessions.csv
        
    Returns:
        pd.DataFrame: DataFrame containing game session data
        
    Raises:
        FileNotFoundError: If CSV file not found
        ValueError: If data validation fails
    """
    if filepath is None:
        # Get the project root directory
        project_root = Path(__file__).parent.parent
        filepath = project_root / 'data' / 'game_sessions.csv'
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Game sessions file not found: {filepath}")
    
    df = pd.read_csv(filepath)
    
    # Validate required columns
    required_columns = ['SessionName', 'Player', 'Character', 'ActionType', 
                       'TargetNum', 'RollDate', 'RollTime', 'RollOutcome']
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Data type conversions
    df['RollDate'] = pd.to_datetime(df['RollDate'])
    df['RollTime'] = pd.to_timedelta(df['RollTime']) 
    df['TargetNum'] = pd.to_numeric(df['TargetNum'], errors='coerce')
    
    return df

def validate_data(df):
    """
    Validate the structure and content of game session data.
    
    Args:
        df (pd.DataFrame): DataFrame to validate
        
    Returns:
        dict: Validation report with statistics
    """
    report = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'missing_values': df.isnull().sum().to_dict(),
        'unique_sessions': df['SessionName'].nunique(),
        'unique_players': df['Player'].nunique(),
        'unique_actions': df['ActionType'].nunique(),
        'outcome_distribution': df['RollOutcome'].value_counts().to_dict()
    }
    return report

if __name__ == "__main__":
    df = load_game_sessions()
    print(f"Loaded {len(df)} game session records")
    print(f"\nData shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nFirst few rows:")
    print(df.head())
    
    # Print validation report
    report = validate_data(df)
    print(f"\nValidation Report:")
    for key, value in report.items():
        print(f"{key}: {value}")
