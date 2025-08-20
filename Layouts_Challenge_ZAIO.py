from bokeh.plotting import figure, show
from bokeh.layouts import row, column, gridplot
def create_bokeh_layouts():
    """
    Create multiple plots and arrange them using Bokeh layouts.

    Args:
    None

    Returns:
    tuple: A tuple containing the row, column, and grid layouts.
    """
    # YOUR CODE HERE
    sales_city1 = [29909, 31956, 34527, 37520, 38945, 42904]
    sales_city2 = [23112, 24324, 25646, 25879, 26342, 26903]
    sales_city3 = [32110, 35319, 37459, 38784, 38765, 37632]
    years = [2016, 2017, 2018, 2019, 2020, 2021]
    s1 = figure(width=250, height=250, background_fill_color="#fafafa")
    s1.scatter(years, sales_city1, size=12,marker='circle', color="#53778a", fill_alpha=0.8)

    s2 = figure(width=250, height=250, background_fill_color="#fafafa")
    s2.scatter(years, sales_city2, size=12,marker='triangle', color="#c02942", fill_alpha=0.8)

    s3 = figure(width=250, height=250, background_fill_color="#fafafa")
    s3.scatter(years, sales_city3, size=12,marker='square', color="#d95b43", fill_alpha=0.8)

    row_layout = row(s1, s2, s3)
    column_layout = column(s1, s2, s3)
    grid_layout = gridplot([[s1, s2], [s3, None]])

    return {"Row": row_layout, "Column": column_layout, "Grid": grid_layout}

# print(create_bokeh_layouts())
layouts = create_bokeh_layouts()
show(layouts["Row"])     # side by side
show(layouts["Column"])  # stacked
show(layouts["Grid"])    # 2x2 grid
