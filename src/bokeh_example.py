"""Example using Bokeh to create interactive visualizations."""

import pandas as pd
from data_loader import load_game_sessions
from bokeh.plotting import figure, output_file, save
from bokeh.models import HoverTool
from bokeh.transform import dodge, cumsum
from bokeh.palettes import Category20
from math import pi

def create_bokeh_html():
    """Create interactive visualizations using Bokeh."""
    df = load_game_sessions()
    
    # Create a pivot table for outcomes by session
    pivot_data = df.groupby(['SessionName', 'RollOutcome']).size().reset_index(name='Count')
    
    # Get unique outcomes and sessions
    outcomes = pivot_data['RollOutcome'].unique()
    sessions = pivot_data['SessionName'].unique()
    
    # Create output file
    output_file('docs/bokeh.html')
    
    # Create figure
    p = figure(
        x_range=list(sessions),
        title='RPG Roll Outcomes by Session',
        toolbar_location='right',
        tools='pan,wheel_zoom,box_zoom,reset,save',
        width=1000,
        height=600
    )
    
    # Define colors
    colors = Category20[len(outcomes)]
    color_map = {outcome: colors[i] for i, outcome in enumerate(outcomes)}
    
    # Plot grouped bars for each outcome
    offset = 0
    bar_width = 0.2
    num_outcomes = len(outcomes)
    
    for i, outcome in enumerate(outcomes):
        outcome_data = pivot_data[pivot_data['RollOutcome'] == outcome]
        offset_amount = (i - num_outcomes/2 + 0.5) * bar_width
        
        p.vbar(
            x=dodge('SessionName', offset_amount, range=p.x_range),
            top='Count',
            width=bar_width,
            source=outcome_data,
            color=color_map[outcome],
            legend_label=outcome,
            alpha=0.8
        )
    
    # Customize appearance
    p.xaxis.axis_label = 'Session'
    p.yaxis.axis_label = 'Number of Rolls'
    p.legend.location = 'top_right'
    p.legend.click_policy = 'hide'
    p.xaxis.major_label_orientation = pi/4
    
    # Add hover tool
    hover = HoverTool(tooltips=[('Session', '@SessionName'), ('Count', '@Count')])
    p.add_tools(hover)
    
    # Save to HTML
    save(p)
    print("Created docs/bokeh.html")

if __name__ == "__main__":
    create_bokeh_html()
