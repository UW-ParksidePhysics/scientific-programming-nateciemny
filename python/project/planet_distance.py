"""
This code makes scale models of the distance planets are from the Sun using a ruler. There are a total of 44 output
png files for the different versions of the ruler. There are a total of 11 objects that I have coded the distances for.
There are four variants for each object. The variants are as follows: a 3.5 inch black and white model, a 1.5 inch black
and white model, a 3.5 inch colored model, and a 1.5 inch colored model. This program ensures that it is compatible with
Mac and Windows for convenience. The diameters, in size, are relative to jupiter in order to create consistent markers.
 The main goal of all this code is to give a brief visual for how far each planet is from the sun in astronomical units.

 The code was made originally by Professor William Parker in this folder:
https://github.com/williamdparker/AstronomyCalculations/tree/master/solar_system_sign_icons
I have made edits in order to create multiple variants of the ruler.

"""
__author__ = "Nate Ciemny"

import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def read_json_file(data_file):
    """
    Read and return the data from given JSON file.

    Args:
        data_file (str): Path to the JSON file.

    Returns:
        dict: Dictionary of data from JSON file.
    """

    with open(data_file, "r") as file:
        json_data = json.load(file)
    return json_data

def draw_logarithmic_ruler(object_distances, object_diameters, planet_colors, highlight_object, color_scheme="color highlighted", figure_height=5):
    """
  Draw distance ruler with planets scaled to relative diameters.
  Args:
      object_distances (dict): Dictionary of distances between planets.
      object_diameters (dict): Dictionary of diameters between planets.
      planet_colors (dict): Dictionary of colors between planets.
      highlight_object (str): Highlight object.
      color_scheme (bool): If True, convert to color_scheme.
      figure_height (int): Figure height in inches.
    Returns:
        None. Saves file for each version of ruler.
    """

    scale = figure_height / 5 # Relative to 5 inch base

    minimum_distance = min(object_distances.values())
    maximum_distance = max(object_distances.values())

    log_minimum = np.floor(np.log10(minimum_distance))
    log_maximum = np.ceil(np.log10(maximum_distance))

    fig, ax = plt.subplots(figsize=(10, figure_height))
    ax.set_xlim(log_minimum, log_maximum)
    ax.set_ylim(-0.7, 0.5)

    x_limits = ax.get_xlim()
    y_limits = ax.get_ylim()

    x_range = np.diff(x_limits)[0]
    y_range = np.diff(y_limits)[0]

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.add_patch(plt.Rectangle((x_limits[0], y_limits[0]), x_range, 0.5 * y_range, edgecolor='black',
                                facecolor='none', linewidth=5 * scale))

    sun_circle = plt.Circle((log_minimum - 0.35, 0.15), 0.5, color='gold', zorder=1)
    ax.add_patch(sun_circle)
    ax.add_patch(plt.Rectangle((x_limits[0], y_limits[0]), x_range, 0.5 * y_range, edgecolor='black',
                               facecolor='none', linewidth=5 * scale))

    ax.text(log_minimum + 0.1, -0.35, 'AU',
            ha='left', va='center', fontsize=18 * scale, fontname='Arial', color='black')

    ax_top = ax.inset_axes([x_limits[0], y_limits[0] + 0.49 * y_range, x_range, 0.001],
                           transform=ax.transData, zorder=2)

    ax_top.get_yaxis().set_visible(False)
    ax_top.spines['top'].set_visible(False)
    ax_top.spines['right'].set_visible(False)
    ax_top.spines['left'].set_visible(False)

    ax_top.set_xlim(x_limits)
    ax_top.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=10))
    ax_top.set_xticks([np.log10(0.2), np.log10(0.5), 0, np.log10(2), np.log10(5), 1, np.log10(20), np.log10(50)])
    ax_top.set_xticklabels(['0.2', '0.5', '1', '2', '5', '10', '20', '50'])
    ax_top.tick_params(direction='out', length=10 * scale, width=2 * scale, colors='black', pad=5 * scale,
                       top=False, bottom=True, labeltop=False, labelbottom=True,
                       labelsize=24 * scale)

    for tick in ax_top.get_xticklabels():
        tick.set_fontname('Arial')

    jupiter_diameter = 1.42984e5 # Km
    giant_planet_reduction = 8
    small_planet_reduction = 3

    for object, distance in object_distances.items():
        if object in object_diameters:
            diameter = object_diameters[object]
            if log_minimum <= np.log10(distance) <= log_maximum:
                if diameter < 0.1 * jupiter_diameter:
                    radius = diameter / (small_planet_reduction * jupiter_diameter)
                else:
                    radius = diameter / (giant_planet_reduction * jupiter_diameter)

                planet_color = planet_colors.get(object, "black")
                if color_scheme == 'all black':
                    planet_color = "black"
                if color_scheme == 'all color':
                    label_color = planet_color
                else:
                    label_color = "black"

                if object == highlight_object:
                    ax.add_patch(plt.Circle((np.log10(distance), 0.32), radius, color=planet_color, alpha=0.9))

                    label_y = 0.36
                    if object in ["Jupiter", "Saturn"]:
                        label_y = 0.42
                    if object == "Jupiter":
                        label_y = 0.45

                    ax.text(np.log10(distance), label_y, object, ha='center', va='bottom',
                            color=label_color, fontsize=14 * scale, fontname='Arial')

                    if figure_height <= 1.6:
                        arrow_style = f"Fancy,head_length={1 * scale},head_width={0.5 * scale},tail_width={0.25 * scale}"
                    else:
                        arrow_style = f"Fancy,head_length={1.5 * scale},head_width={0.75 * scale},tail_width={0.3 * scale}"

                    ax.annotate('', xy=(np.log10(distance), -0.11),
                                xytext=(np.log10(distance), 0.32 - radius),
                                arrowprops=dict(arrowstyle=arrow_style, color=planet_color))


                else:
                    ax.add_patch(plt.Circle((np.log10(distance), 0.05), radius, color= label_color, alpha=0.9))

    ax.text(log_minimum + 0.1, -0.55,
            "1 AU ≈ 93 million miles ≈ 150 million kilometers",
            ha='left', va='top', fontsize=14 * scale, fontname='Arial')

    ax.set_aspect('equal', 'box')
    ax.set_frame_on(False)

    if color_scheme == 'all black':
        suffix = "_bw"
    elif color_scheme == 'highlight color':
        suffix = '_color'
    else:
        suffix = '_allcolor'
    plt.savefig(f"{highlight_object}{suffix}_{figure_height}in.png", dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    import matplotlib
    import platform

# Used ChatGPT. Prompt: "What would I add to this code so that it can run on both mac and windows depending on which one I use"
    if platform.system() == 'Darwin':  # Mac
        matplotlib.use('macosx')
    else:  # Windows
        matplotlib.use('Agg')

    planetary_distances = read_json_file("semimajor_axes.json")
    planetary_diameters = read_json_file("diameters.json")
    planet_colors = read_json_file("planet_colors.json")

    for planet in planetary_distances.keys():
        for figure_height in [3.5, 1.5]:
            for coloring_scheme in ['all color', 'highlight color', 'all black']:
                print(f"Generating: {planet}, {figure_height}\" figure, scheme: {coloring_scheme}")
                draw_logarithmic_ruler(planetary_distances, planetary_diameters, planet_colors, highlight_object=planet,
                                       color_scheme=coloring_scheme, figure_height=figure_height)
