from bokeh.plotting import figure, show
def customize_bokeh_plot():
    """
    Create and customize a scatter plot using Bokeh.

    Args:
    None

    Returns:
    bokeh.plotting.Figure: The Bokeh figure object containing the customized plot.
    """
    # YOUR CODE HERE
    years = [2016, 2017, 2018, 2019, 2020, 2021]
    sales = [29909, 31956, 34527, 37520, 38945, 42904]
    p = figure(
        title="Customized Sales Plot",
        width=800,  
        height=400,  
        x_axis_label="Year",
        y_axis_label="Sales"
    )

    p.scatter(years, sales, fill_color="red", size=12)
    p.xaxis.axis_line_color = "blue"
    p.xaxis.axis_label_text_color = "green"

    p.yaxis.major_label_orientation = "vertical"
    p.yaxis.axis_label_text_color = "orange"
    show(p)

    return p
print(customize_bokeh_plot())