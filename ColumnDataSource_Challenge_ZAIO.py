from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
def create_columndatasource_plot():
    """
    Create a scatter plot using Bokeh's ColumnDataSource.

    Args:
    None

    Returns:
    bokeh.plotting.Figure: The Bokeh figure object containing the scatter plot.
    """
    # YOUR CODE HERE
    data = {'sales_city3' : [32110, 35319, 37459, 38784, 38765, 37632],
    'years' : [2016, 2017, 2018, 2019, 2020, 2021]}

    source = ColumnDataSource(data=data)
    p = figure(title="City 3 Sales", x_axis_label="Years", y_axis_label="Sales",width=250, height=250, background_fill_color="#fafafa")
    p.scatter(x='years', y='sales_city3', source=source, color='blue')
    show(p)
    return p
print(create_columndatasource_plot())