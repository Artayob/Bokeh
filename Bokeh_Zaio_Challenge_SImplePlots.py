from bokeh.plotting import figure, show
def create_combined_bokeh_plot():
    """
    Create a combined plot with multiple glyphs using Bokeh.

    Args:
    None

    Returns:
    bokeh.plotting.Figure: The Bokeh figure object containing the combined plot.
    """
    # YOUR CODE HERE
    sales_city1 = [29909, 31956, 34527, 37520, 38945, 42904]
    sales_city2 = [23112, 24324, 25646, 25879, 26342, 26903]
    sales_city3 = [32110, 35319, 37459, 38784, 38765, 37632]
    years = [2016, 2017, 2018, 2019, 2020, 2021]

    p = figure(
        title="Sales Data for Multiple Cities",
        x_axis_label="Year",
        y_axis_label="Sales", 
        width=800, 
        height=400
    )
    p.line(years, sales_city1, line_width=2, legend_label="City 1", color='blue')
    p.vbar(x=years, top=sales_city2, legend_label="City 2", width=0.5, bottom=0, color='red')
    p.scatter(years, sales_city3, legend_label="City 3", line_color="yellow", size=10)

    show(p)
    return p
print(create_combined_bokeh_plot())