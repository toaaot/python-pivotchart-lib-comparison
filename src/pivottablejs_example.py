"""Example using PivotTable.js to create interactive pivot tables."""
import json
import pandas as pd
from data_loader import load_game_sessions

def create_pivottablejs_html():
    """Create an interactive pivot table using PivotTable.js."""
    df = load_game_sessions()
    
    # 1. Prepare data: PivotTable.js works best with simple lists of dicts
    # Convert datetime objects to strings so JSON can handle them
    df_export = df.copy()
    if 'RollDate' in df_export.columns:
        df_export['RollDate'] = df_export['RollDate'].dt.strftime('%Y-%m-%d')
    if 'RollTime' in df_export.columns:
        df_export['RollTime'] = df_export['RollTime'].astype(str)

    data_json = df_export.to_dict(orient='records')

    # 2. The Template
    # Note: I used a raw string and .replace() to avoid f-string escaping issues
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>PivotTable.js - RPG Session Analysis</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/pivottable/2.23.0/pivot.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pivottable/2.23.0/pivot.min.css">
        <style>
            body { font-family: Verdana, sans-serif; margin: 20px; background-color: #f4f4f9; }
            h1 { color: #2c3e50; }
            #pivot { margin-top: 20px; background-color: white; padding: 10px; border-radius: 8px; }
        </style>
    </head>
    <body>
        <h1>PivotTable.js - RPG Session Analysis</h1>
        <p>Drag and drop dimensions to analyze RPG game session data.</p>
        <div id="pivot"></div>
        <script type="text/javascript">
            $(function() {
                var data = DATA_PLACEHOLDER;
                $("#pivot").pivotUI(data, {
                    rows: ["SessionName"],
                    cols: ["ActionType"],
                    aggregatorName: "Count",
                    rendererName: "Table"
                });
            });
        </script>
    </body>
    </html>
    """
    
    # 3. Inject data and save
    html_content = html_template.replace('DATA_PLACEHOLDER', json.dumps(data_json))
    with open('docs/pivottablejs.html', 'w') as f:
        f.write(html_content)

    print("Created docs/pivottablejs.html")

if __name__ == "__main__":
    create_pivottablejs_html()
