import pandas as pd 
import numpy as np

from bokeh.io import output_file 
from bokeh.layouts import layout, row
from bokeh.plotting import figure, show

from bokeh.models import ColumnDataSource, Div, RangeSlider, Spinner

sales_city1 = [29909, 31956, 34527, 37520, 38945, 42904]
sales_city2 = [23112, 24324, 25646, 25879, 26342, 26903]
sales_city3 = [32110, 35319, 37459, 38784, 38765, 37632]
years = [2016, 2017, 2018, 2019, 2020, 2021]

s1 = figure(width=250, height=250, background_fill_color="#fafafa")
s1.circle(years, sales_city1, size=12, color="#53778a", fill_alpha=0.8)

s2 = figure(width=250, height=250, background_fill_color="#fafafa")
s2.triangle(years, sales_city2, size=12, color="#c02942", fill_alpha=0.8)

s3 = figure(width=250, height=250, background_fill_color="#fafafa")
s3.square(years, sales_city3, size=12, color="#d95b43", fill_alpha=0.8)  # fixed typo

# Display side by side
# show(row(s1, s2, s3))

# from bokeh.layouts import column 
# show(column(s1, s2, s3))

from bokeh.layouts import gridplot
grid = gridplot([[s1, None, s2], [None, s3, None]], width=300, height=300)

show(grid)