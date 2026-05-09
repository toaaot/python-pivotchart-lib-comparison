"""Example using Plotly to create interactive charts."""

import pandas as pd
import plotly.express as px
from data_loader import load_game_sessions

def create_plotly_html():
    """Create interactive visualizations using Plotly, mit separater JS-Datei für Offline-Nutzung"""
    df = load_game_sessions()
    
    # Create a pivot table
    pivot_data = df.groupby(['SessionName', 'RollOutcome']).size().reset_index(name='Count')
    
    # Create Plotly figure
    fig = px.bar(
        pivot_data,
        x='SessionName',
        y='Count',
        color='RollOutcome',
        title='RPG Roll Outcomes by Session',
        labels={'Count': 'Number of Rolls', 'SessionName': 'Session'},
        barmode='group'
    )
    
    fig.update_layout(
        width=1000,
        height=600,
        hovermode='x unified',
        xaxis_tickangle=-45
    )
    
    # Save to HTML
    # erstellt eine separate 4 MB Datei "plotly.min.js"
    fig.write_html('docs/plotly.html', include_plotlyjs='directory')

    print("Created docs/plotly.html and docs/plotly.min.js")

if __name__ == "__main__":
    create_plotly_html()
