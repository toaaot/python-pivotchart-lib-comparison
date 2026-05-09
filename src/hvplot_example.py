"""Example using hvPlot to create interactive visualizations."""
import pandas as pd
import hvplot
import hvplot.pandas
from data_loader import load_game_sessions

def create_hvplot_html():
    """Create interactive visualizations using hvPlot."""
    df = load_game_sessions()
    
    # Create a pivot table
    pivot_data = df.groupby(['SessionName', 'ActionType']).size().unstack(fill_value=0)
    
    # Create hvplot visualization
    plot = pivot_data.hvplot.bar(
        title='RPG Actions by Session',
        xlabel='Session',
        ylabel='Count',
        rot=45,
        width=1000,
        height=600
    )
    
    # Save directly to a self-contained HTML file
    # This automatically includes the necessary Bokeh/JS resources
    hvplot.save(plot, 'docs/hvplot.html')
    
    print("Created docs/hvplot.html")

if __name__ == "__main__":
    create_hvplot_html()
