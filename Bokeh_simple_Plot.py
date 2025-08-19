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

p = figure(title="Multiple glyphs example", x_axis_label="x", y_axis_label="y")

p.line(years, sales_city1, legend_label="City 1", line_color='blue', line_width=2)
p.vbar(x=years, top=sales_city2, legend_label="City 2", width=0.5, bottom=0, color='red')
p.circle(years, sales_city3, legend_label="City 3", line_color="yellow", size=10)

show(p)