import pandas as pd
import numpy as np

from bokeh.io import output_file
from bokeh.layouts import layout
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Div, RangeSlider, Spinner

gm_data = pd.read_csv("C:/Users/sakit/Desktop/Bokeh/gapminder_data_graphs.csv")

latestrecs = gm_data.loc[gm_data['year'] == 2007]
print(latestrecs)

x = latestrecs['life_exp']
y = latestrecs['gdp']

output_file("gapminder-with-widgets.html")

p = figure(x_range=(1, len(x)), width=500, height=250)
points = p.scatter(x=x, y=y, size=7, fill_color="#21a7df")  # scatter instead of circle

spinner = Spinner(
    title="Circle size",
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,
    width=200
)
spinner.js_link("value", points.glyph, "size")

range_slider = RangeSlider(
    title="Adjust x-axis range",
    start=0,
    end=180,
    step=1,
    value=(p.x_range.start, p.x_range.end)
)
range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

show(layout([[spinner], [range_slider], [p]]))
