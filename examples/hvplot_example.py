"""Example using hvPlot to create interactive visualizations."""
import pandas as pd
from src.data_loader import load_game_sessions
import hvplot.pandas

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
    
    # Save to HTML
    from bokeh.embed import file_html
    from bokeh.resources import CDN
    import holoviews as hv
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>hvPlot - RPG Session Analysis</title>
        <script src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.3.min.js"></script>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
        </style>
    </head>
    <body>
        <h1>hvPlot - RPG Session Analysis</h1>
        <p>Interactive bar chart of RPG actions by session.</p>
        <div id="plot"></div>
    </body>
    </html>
    """
    
    with open('docs/hvplot.html', 'w') as f:
        f.write(html_content)
    print("Created docs/hvplot.html")

if __name__ == "__main__":
    create_hvplot_html()
