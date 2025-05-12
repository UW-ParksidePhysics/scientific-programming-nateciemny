"""
Annotate a plot using Pyplot's text function.
Draws label strings at specified positions with alignment and font size.
"""

__author__ = "Nate Ciemny"

import matplotlib.pyplot as pyplot
import datetime


def annotate_plot(annotations):
    """
    Add annotations to a plot using label text and formatting information.

    Parameters:
        annotations: dictionary with label strings as keys and value dictionaries that include:
            - 'position': (x, y) coordinates for placement
            - 'alignment': [horizontal, vertical] alignments
            - 'fontsize': font size in pixels

    Returns:
        None
    """
    for label_text, label_properties in annotations.items():
        x_position, y_position = label_properties['position']
        horizontal_alignment, vertical_alignment = label_properties['alignment']
        font_size = label_properties['fontsize']

        pyplot.text(
            x_position,
            y_position,
            label_text,
            ha=horizontal_alignment,
            va=vertical_alignment,
            fontsize=font_size
        )


if __name__ == "__main__":
    # Create a sample plot
    x_values = [0, 1, 2, 3]
    y_values = [0, 1, 4, 9]
    pyplot.plot(x_values, y_values)

    # Today's date in ISO 8601 format
    today_date = datetime.datetime.now().date().isoformat()

    label = f"Created by Nate Ciemny {today_date}"

    # Place text using figure coordinates
    pyplot.gcf().text(
        0.01,
        0.01,
        label,
        ha='left',
        va='bottom',
        fontsize=10
    )

    pyplot.show()

