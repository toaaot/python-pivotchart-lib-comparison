"""Example using PivotTable.js to create interactive pivot tables."""
import pandas as pd
from src.data_loader import load_game_sessions
import json

def create_pivottablejs_html():
    """Create an interactive pivot table using PivotTable.js."""
    df = load_game_sessions()
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>PivotTable.js - RPG Session Analysis</title>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pivottable/2.23.0/pivot.min.js"></script>
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.css">
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/pivottable/2.23.0/pivot.min.css">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            #pivot { margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>PivotTable.js - RPG Session Analysis</h1>
        <p>Drag and drop dimensions to analyze RPG game session data.</p>
        <div id="pivot"></div>
        <script type="text/javascript">
            var data = {DATA_PLACEHOLDER};
            $(function() {{
                $("#pivot").pivotUI(data, {{
                    rows: ["SessionName"],
                    cols: ["ActionType"],
                    vals: ["RollOutcome"],
                    aggregatorName: "Count",
                    rendererName: "Table"
                }});
            }});
        </script>
    </body>
    </html>
    """
    
    # Convert DataFrame to JSON
    data_json = df.to_dict(orient='records')
    html_content = html_template.replace('{DATA_PLACEHOLDER}', json.dumps(data_json))
    
    # Write to file
    with open('docs/pivottablejs.html', 'w') as f:
        f.write(html_content)
    print("Created docs/pivottablejs.html")

if __name__ == "__main__":
    create_pivottablejs_html()
