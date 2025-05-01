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

# Pull out the planet circle draw into a separate function in order to bump out individual planets and maybe
# draw an arrow from the planet to the ruler below

import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import platform

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

def draw_logarithmic_ruler(object_distances, object_diameters, planet_colors, highlight_object, grayscale=False, fig_height=5):
    """
  Draw distance ruler with planets scaled to relative diameters.

  Args:
      object_distances (dict): Dictionary of distances between planets.
      object_diameters (dict): Dictionary of diameters between planets.
      planet_colors (dict): Dictionary of colors between planets.
      highlight_object (str): Highlight object.
      grayscale (bool): If True, convert to grayscale.
      fig_height (int): Figure height in inches.

    Returns:
        None. Saves file for each version of ruler.

    """
    # Scaling factor based on figure height
    scale = fig_height / 5 # Scaling factor relative to 5 inch base

    # Calculate the extreme distance values
    min_distance = min(object_distances.values())
    max_distance = max(object_distances.values())

    # Define the range for the logarithmic scale
    log_min = np.floor(np.log10(min_distance))
    log_max = np.ceil(np.log10(max_distance))

    # Generate the logarithmic ruler
    fig, ax = plt.subplots(figsize=(10, fig_height))
    ax.set_xlim(log_min, log_max)
    ax.set_ylim(-0.7, 0.5)

    x_limits = ax.get_xlim()
    y_limits = ax.get_ylim()

    x_range = np.diff(x_limits)[0]
    y_range = np.diff(y_limits)[0]

    # Hide x-axis
    ax.get_xaxis().set_visible(False)
    # Hide y-axis
    ax.get_yaxis().set_visible(False)

    # Draw rectangle representing the ruler background
    ax.add_patch(plt.Rectangle((x_limits[0], y_limits[0]), x_range, 0.5 * y_range, edgecolor='black',
                                facecolor='none', linewidth=5 * scale))

    # Label the ruler units as AU
    ax.text(log_min + 0.1, -0.35, 'AU',
            ha='left', va='center', fontsize=18 * scale, fontname='Arial', color='black')

    # Add axis at top of rectangle
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

    # Available Fonts
    # ['STIXSizeFourSym', 'DejaVu Sans Display', 'STIXNonUnicode', 'cmss10', 'STIXNonUnicode', 'DejaVu Sans Mono',
    #  'DejaVu Sans Mono', 'DejaVu Sans', 'DejaVu Serif Display', 'STIXSizeTwoSym', 'STIXSizeTwoSym', 'STIXGeneral',
    #  'STIXGeneral', 'STIXGeneral', 'cmmi10', 'STIXSizeOneSym', 'cmr10', 'DejaVu Sans', 'cmtt10', 'DejaVu Sans',
    #  'DejaVu Serif', 'STIXSizeThreeSym', 'STIXSizeOneSym', 'STIXSizeFourSym', 'STIXNonUnicode', 'cmex10', 'cmb10',
    #  'STIXSizeFiveSym', 'DejaVu Sans', 'DejaVu Sans Mono', 'STIXNonUnicode', 'STIXSizeThreeSym', 'DejaVu Sans Mono',
    #  'cmsy10', 'DejaVu Serif', 'DejaVu Serif', 'DejaVu Serif', 'STIXGeneral', 'Apple SD Gothic Neo', 'Zapf Dingbats',
    #  'Noto Nastaliq Urdu', 'Diwan Thuluth', 'Athelas', 'AppleGothic', 'Noto Sans Cypriot', 'Georgia', 'Galvji',
    #  'Myanmar MN', 'Charter', 'STIXNonUnicode', 'Hiragino Sans', 'STIXIntegralsUpD', 'Verdana', 'Kohinoor Gujarati',
    #  'DecoType Naskh', 'Plantagenet Cherokee', 'Noto Sans Cham', 'DIN Alternate', 'Hoefler Text', 'Comic Sans MS',
    #  'Noto Sans Sharada', 'Noto Sans Tifinagh', 'Cochin', 'STIXGeneral', 'Hiragino Sans', 'Noto Sans Old North Arabian',
    #  'Noto Sans Lydian', 'Noto Sans Siddham', 'Noto Sans Palmyrene', 'STIXSizeFiveSym', 'Noto Sans Linear A',
    #  'Noto Sans Tai Le', 'Mshtakan', 'Noto Sans Old Italic', 'Noto Sans PhagsPa', 'Arial Unicode MS', 'Courier New',
    #  'American Typewriter', 'Noto Sans Ol Chiki', 'ITF Devanagari', 'Snell Roundhand', 'Apple Braille', 'Al Bayan',
    #  'Arial Black', 'Songti SC', 'Georgia', 'Noto Sans Yi', 'Chalkduster', 'Noto Serif Yezidi', 'Noto Sans Hatran',
    #  'Arial', 'Noto Sans Khudawadi', 'Apple Braille', 'Bradley Hand', 'Hiragino Sans', 'Optima', 'Phosphate', 'Avenir',
    #  'Kohinoor Bangla', 'Savoye LET', 'InaiMathi', 'Times New Roman', 'Noto Sans Javanese', 'Impact',
    #  'Kannada Sangam MN', 'Marker Felt', 'STIXSizeTwoSym', 'Webdings', 'Oriya Sangam MN', 'PT Sans', 'STIXSizeFourSym',
    #  'Geeza Pro', 'Tamil MN', 'Gurmukhi MN', 'Georgia', 'Avenir Next Condensed', 'Noto Sans Limbu', 'STIXIntegralsUp',
    #  'Luminari', 'Verdana', '.SF NS Mono', 'Noto Sans Duployan', 'Arial Narrow', 'Arial Narrow', 'Academy Engraved LET',
    #  'New Peninim MT', 'Arial Narrow', 'Noto Sans Wancho', 'Tamil Sangam MN', 'Noto Sans Masaram Gondi',
    #  'Noto Sans Marchen', 'Kohinoor Devanagari', 'Noteworthy', 'Verdana', 'Noto Sans Brahmi', 'Apple Braille',
    #  'Noto Sans Buhid', 'Gurmukhi Sangam MN', 'Malayalam Sangam MN', 'Brush Script MT', 'Helvetica', 'PT Serif',
    #  'Big Caslon', 'Noto Sans Gunjala Gondi', 'Bodoni Ornaments', 'Trebuchet MS', 'Bangla MN', 'Herculanum',
    #  'Hiragino Maru Gothic Pro', 'AppleMyungjo', 'Comic Sans MS', 'Noto Sans NKo', 'Noto Sans Bhaiksuki',
    #  'Noto Sans Meetei Mayek', 'Al Tarikh', 'Times New Roman', 'Noto Sans Avestan', 'Baghdad', 'Noto Sans Syriac',
    #  'Krungthep', 'Monaco', 'STIXSizeOneSym', 'System Font', 'Noto Sans Multani', 'Noto Serif Myanmar',
    #  'Noto Sans Bassa Vah', '.SF Compact', 'Baskerville', 'Euphemia UCAS', 'Hiragino Sans', 'Marion', 'STIXSizeFourSym',
    #  'Noto Sans Modi', 'Noto Sans Mende Kikakui', 'Noto Sans Glagolitic', 'Bodoni 72 Smallcaps', 'Heiti TC', 'Geneva',
    #  'Noto Sans Tai Tham', 'Noto Sans Mongolian', 'Noto Sans Tai Viet', 'Nadeem', 'Seravek', 'Times New Roman',
    #  '.SF Compact Rounded', 'Corsiva Hebrew', 'Noto Sans Bamum', 'Farah', 'Noto Sans Rejang', 'Menlo',
    #  'Noto Sans Buginese', 'Hiragino Sans', 'Noto Sans Old Hungarian', 'Noto Sans Cuneiform', 'Andale Mono', 'Khmer MN',
    #  'Noto Sans Carian', 'Courier', 'Avenir Next', 'KufiStandardGK', 'Noto Sans Adlam', 'Kailasa',
    #  'Noto Sans Kharoshthi', 'STIXGeneral', 'Courier New', 'Farisi', 'Helvetica Neue', '.Keyboard',
    #  'Noto Serif Balinese', 'Noto Sans Caucasian Albanian', 'Trattatello', 'Sathu', 'Noto Sans Tagalog',
    #  'Noto Sans Osmanya', 'Noto Sans Miao', 'Noto Sans Phoenician', 'Devanagari Sangam MN', 'Hiragino Mincho ProN',
    #  'Noto Sans Hanifi Rohingya', 'Bodoni 72 Oldstyle', 'STIXVariants', 'Diwan Kufi', 'Noto Sans Egyptian Hieroglyphs',
    #  'Rockwell', 'Noto Sans Lycian', 'Futura', 'Noto Sans Pau Cin Hau', 'Noto Sans Ugaritic', 'STIXSizeOneSym',
    #  '.New York', 'STIXGeneral', 'Noto Sans Manichaean', 'STIXSizeTwoSym', 'Lao MN', 'Noto Sans Mro', 'Devanagari MT',
    #  'Wingdings 3', 'STIXGeneral', 'Noto Sans Meroitic', 'Gujarati Sangam MN', 'Apple Symbols', 'Noto Sans Warang Citi',
    #  'Wingdings 2', 'Didot', 'STIXIntegralsSm', 'Hiragino Sans', '.New York', 'Myanmar Sangam MN', 'Zapfino',
    #  'STIXNonUnicode', 'Shree Devanagari 714', 'Copperplate', 'Noto Sans Newa', 'Verdana', 'Noto Sans Thaana',
    #  'STIXIntegralsUpSm', 'Arial', 'Gujarati MT', 'STIXIntegralsD', 'Noto Sans Osage', 'Arial Rounded MT Bold', 'Arial',
    #  'Hiragino Sans', 'Wingdings', 'Malayalam MN', 'Arial Unicode MS', 'Courier New', 'DIN Condensed',
    #  'Noto Serif Ahom', 'System Font', 'Noto Sans Pahawh Hmong', 'Hiragino Sans GB', 'Heiti TC', 'Apple Braille',
    #  'Noto Sans Batak', 'Ayuthaya', 'Noto Sans Mandaic', 'Tahoma', 'Noto Sans Kayah Li', 'Noto Sans Linear B',
    #  'Bodoni 72', 'Lucida Grande', 'Noto Sans Coptic', '.SF NS Mono', 'Iowan Old Style', 'Hoefler Text', 'Courier New',
    #  'Hiragino Sans', 'Hiragino Sans', 'Kannada MN', 'Sana', 'Khmer Sangam MN', 'Tahoma', 'Noto Sans Tirhuta',
    #  'Thonburi', 'Chalkboard SE', 'Noto Sans Armenian', 'STIXNonUnicode', 'Gill Sans', 'Hiragino Sans', 'Apple Braille',
    #  'Silom', 'Palatino', 'Noto Sans Imperial Aramaic', 'Waseem', 'Kokonor', '.SF Arabic', 'Gurmukhi MT',
    #  'Noto Sans Khojki', 'Oriya MN', 'Noto Sans Elbasan', 'Mishafi', 'Noto Sans Syloti Nagri', 'Noto Sans Chakma',
    #  'Noto Sans Lisu', 'Noto Sans Old Persian', 'Kohinoor Telugu', 'Trebuchet MS', 'Georgia', 'STIXNonUnicode',
    #  'Noto Sans Old South Arabian', 'Noto Sans Nabataean', 'Noto Sans Vai', 'Chalkboard', 'Sinhala MN', 'PT Mono',
    #  'Mukta Mahee', 'Sinhala Sangam MN', 'STIXSizeThreeSym', '.SF NS Rounded', 'Beirut', 'Noto Sans Gothic',
    #  'Trebuchet MS', 'Noto Sans Kaithi', 'Superclarendon', 'Telugu Sangam MN', 'Lao Sangam MN', 'STIXIntegralsD',
    #  'Noto Sans Samaritan', 'Kefa', 'Noto Sans Old Turkic', 'Noto Sans Oriya', 'STIXSizeThreeSym', 'Apple Chancery',
    #  'Noto Sans Inscriptional Parthian', 'STIXIntegralsUpD', 'Noto Sans Myanmar', 'Raanana', 'PingFang HK', 'Skia',
    #  'Al Nile', 'Arial Hebrew', 'Telugu MN', 'Noto Sans Sundanese', 'Noto Sans Hanunoo', 'Noto Sans Lepcha',
    #  'Sukhumvit Set', 'STIXIntegralsSm', 'SignPainter', '.Aqua Kana', 'Noto Sans Tagbanwa', 'Noto Sans Old Permic',
    #  'Muna', 'STIXIntegralsUpSm', 'Noto Sans Sora Sompeng', 'Times New Roman', 'Mishafi Gold', 'Noto Sans Kannada',
    #  'Times', 'Party LET', 'Bangla Sangam MN', 'Damascus', 'PT Serif Caption', 'STIXIntegralsUp',
    #  'Microsoft Sans Serif', 'Symbol', 'Noto Sans Psalter Pahlavi', 'Arial Narrow', '.SF Compact',
    #  'Noto Sans Inscriptional Pahlavi', 'Arial', 'Trebuchet MS', 'Noto Sans New Tai Lue', 'STIXVariants',
    #  'Noto Sans Saurashtra', 'Papyrus', 'Noto Sans Mahajani', 'Noto Sans Takri']
    #
    # Add object names as annotations below the ticks
    # for obj, dist in object_distances.items():
    #     if log_min <= np.log10(dist) <= log_max:
    #         ax.annotate(obj, (dist, -0.25), ha='center', va='top', fontsize=8, rotation=45)
    jupiter_diameter = 1.42984e5  # Km
    giant_planet_reduction = 8  # Scale for large planets
    small_planet_reduction = 3  # Scale for small planets

    for obj, dist in object_distances.items():
        if obj in object_diameters:
            diameter = object_diameters[obj]
            if log_min <= np.log10(dist) <= log_max:
                if diameter < 0.1 * jupiter_diameter:
                    radius = diameter / (small_planet_reduction * jupiter_diameter)
                else:
                    radius = diameter / (giant_planet_reduction * jupiter_diameter)

                planet_color = planet_colors.get(obj, "black")
                if grayscale:
                    planet_color = "black"

                if obj == highlight_object:
                    ax.add_patch(plt.Circle((np.log10(dist), 0.32), radius, color=planet_color, alpha=0.9))

                    label_y = 0.36
                    if obj in ["Jupiter", "Saturn"]:
                        label_y = 0.42
                    if obj == "Jupiter":
                        label_y = 0.45

                    label_color = planet_color if not grayscale else "black"

                    ax.text(np.log10(dist), label_y, obj, ha='center', va='bottom',
                            color=label_color, fontsize=14 * scale, fontname='Arial')

                    ax.annotate('', xy=(np.log10(dist), -0.12),
                                xytext=(np.log10(dist), 0.32 - radius),
                                arrowprops=dict(facecolor=planet_color, edgecolor=planet_color, shrink=0.05,
                                                width=2 * scale,
                                                headwidth=8 * scale))

                else:
                    ax.add_patch(plt.Circle((np.log10(dist), 0.05), radius, color='black', alpha=0.9))

    # Add conversion legend for AU to miles and kilometers
    ax.text(log_min + 0.1, -0.55,
            "1 AU ≈ 92.96 million miles ≈ 149.6 million kilometers",
            ha='left', va='top', fontsize=14 * scale, fontname='Arial')

    ax.set_aspect('equal', 'box')
    ax.set_frame_on(False)

    suffix = "_bw" if grayscale else "_color"
    plt.savefig(f"{highlight_object}{suffix}_{fig_height}in.png", dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    import matplotlib
    import platform

    if platform.system() == 'Darwin':  # Mac
        matplotlib.use('macosx')
    else:  # Windows or Linux
        matplotlib.use('Agg')

    planetary_distances = read_json_file("semimajor_axes.json")
    planetary_diameters = read_json_file("diameters.json")
    planet_colors = read_json_file("planet_colors.json")

    for planet in planetary_distances.keys():
        for fig_height in [3.5, 1.5]:
            draw_logarithmic_ruler(planetary_distances, planetary_diameters, planet_colors, highlight_object=planet,
                                   grayscale=False, fig_height=fig_height)
            draw_logarithmic_ruler(planetary_distances, planetary_diameters, planet_colors, highlight_object=planet,
                                   grayscale=True, fig_height=fig_height)

# test_plot()

#### RENAME from planet_distance.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing project ~ 100-200 words
# 2. Module imports that are used in multiple functions
# 3. Function definitions
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order:
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8:
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution
#		visualization
