from bokeh.plotting import figure, show

def create_bokeh_line_plot():
    """
    Create interactive single and multi-line plots using Bokeh.

    Args:
    None

    Returns:
    bokeh.plotting.Figure: The Bokeh figure object containing the line plots.
    """
    # YOUR CODE HERE
    years = [2016, 2017, 2018, 2019, 2020, 2021]
    sales = [29909, 31956, 34527, 37520, 38945, 42904]
    region1_sales = [28000, 30000, 32000, 35000, 37000, 41000]
    region2_sales = [27000, 31000, 34000, 36000, 39000, 42000]

    # Create figure
    p = figure(
        title="Yearly Sales Trend",
        x_axis_label="Year",
        y_axis_label="Sales",
        width=800,   # corrected
        height=400   # corrected
    )
    p.line(years, sales, line_width=2, color="blue", legend_label="Sales Trend")
    p.line(years, region1_sales, line_width=2, color="green", legend_label="Region 1", line_dash="dashed")
    p.line(years, region2_sales, line_width=2, color="red", legend_label="Region 2", line_dash="dotted")

    p.legend.location = "top_left"
    p.legend.click_policy = "hide"

    show(p)

    return p
print(create_bokeh_line_plot())