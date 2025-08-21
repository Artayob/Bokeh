import pandas as pd
import numpy as np

from bokeh.io import output_file
from bokeh.layouts import layout
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Div, RangeSlider, Spinner
from bokeh.models import GMapOptions
from bokeh.plotting import gmap

output_file("London.html")

map_options = GMapOptions(lat=51.5074, lng=-0.1278, map_type="roadmap", zoom=9)




p= gmap("", map_options, title="London")
source = ColumnDataSource(
    data=dict(lat=[51.697301, 51.688377, 51.293971, 51.334749],
              lon=[-0.444855, -0.098305, -0.297686, -0.154442])
)

p.scatter(x="lon", y="lat", size=15, fill_color="red", fill_alpha=0.6, source=source)

show(p)