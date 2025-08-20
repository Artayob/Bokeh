from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show

data =  {'sales_city3' : [32110, 35319, 37459, 38784, 38765, 37632],
         'years' :  [2016, 2017, 2018, 2019, 2020, 2021]}

source = ColumnDataSource(data=data)

p = figure(width=250, height=250, background_fill_color="#fafafa")
p.scatter(x='years', y='sales_city3', source=source)
show(p)