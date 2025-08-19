import pandas as pd 
import numpy as np

from bokeh.io import output_file 
from bokeh.layouts import layout 
from bokeh.plotting import figure, show

from bokeh.models import ColumnDataSource 
from bokeh.models import Div, RangeSlider, Spinner

sales_city1 = [29909, 31956, 34527, 37520, 38945, 42904]
sales_city2 = [23112, 24324, 25646, 25879, 26342, 26903]
sales_city3 = [32110, 35319, 37459, 38784, 38765, 37632]
years = [2016, 2017, 2018, 2019, 2020, 2021]

p = figure(
    title="Plot responsive sizing example",
    sizing_mode="stretch_width",
    height=400,   # ✅ fixed
    width=800,    # ✅ fixed
    x_axis_label="Years",
    y_axis_label="Sales",
)

# add circle renderer
circle = p.circle(years, sales_city1, fill_color="red", size=10)

# change some things about the x-axis
p.xaxis.axis_label = "Years"
p.xaxis.axis_line_width = 1
p.xaxis.axis_line_color = "red"

# change some things about the y-axis
p.yaxis.axis_label = "Sales"
p.yaxis.major_label_text_color = "orange" 
p.yaxis.major_label_orientation = "vertical"

show(p)
