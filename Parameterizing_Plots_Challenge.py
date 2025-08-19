from bokeh.plotting import figure, show
def parameterize_bokeh_scatter_plot():
    """
    Create a scatter plot with parameterized size and color using Bokeh.

    Args:
    None

    Returns:
    bokeh.plotting.Figure: The Bokeh figure object containing the scatter plot.
    """
    # YOUR CODE HERE
    gdp = [5000, 10000, 15000, 20000, 25000, 30000]
    life_expectancy = [50, 55, 60, 65, 70, 75]
    population = [10, 50, 100, 200, 500, 1000]

    p = figure(
        title="GDP vs Life Expectancy (Bubble Size: Population)",
        width=800,
        height=400,
        x_axis_label="GDP (in USD)",
        y_axis_label="Life Expectancy (Years)"
    )
    p.scatter(gdp, life_expectancy, size=[p/20 for p in population], alpha=0.6)

    show(p)
    return p
print(parameterize_bokeh_scatter_plot())