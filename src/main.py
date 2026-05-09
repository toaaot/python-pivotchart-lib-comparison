"""main.py"""

from bokeh_example import create_bokeh_html
from hvplot_example import create_hvplot_html
from pivottablejs_example import create_pivottablejs_html
from plotly_example import create_plotly_html

def main():
    create_bokeh_html()
    create_hvplot_html()
    create_pivottablejs_html()
    create_plotly_html()
    return

if __name__ == "__main__":
    print("--------------------------------------------")
    main()
    print("--------------------------------------------")
    
# end of file
