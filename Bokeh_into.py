import pandas as pd 
import numpy as np

from bokeh.io import output_file 
from bokeh.layouts import layout 
from bokeh.plotting import figure, show

from bokeh.models import ColumnDataSource 
from bokeh.models import Div, RangeSlider, Spinner

sales = [29909, 31956, 34527, 37520, 38945, 42904]
years = [2016, 2017, 2018, 2019, 2020, 2021]

p = figure(title="Simple Line Example", x_axis_label="Year", y_axis_label="Sales")

p.line(years, sales, legend_label="Sales Treand", line_width=3)

show(p)