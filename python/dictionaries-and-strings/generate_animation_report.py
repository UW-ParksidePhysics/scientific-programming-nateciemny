def parse_animation_code(code_filename):
    with open(code_filename, 'r') as file:
        code = file.read()
    snippets = code.split('\n\n')  # break into logical code blocks
    return '\n'.join(f"<pre>{s}</pre>" for s in snippets)


def format_section_header(header_string):
    return f"<h1>{header_string}</h1>"


def write_html_report(report_string, report_filename):
    with open(report_filename, 'w') as file:
        file.write(report_string)


def create_html_report(code_filename, plot_filenames, gif_filename, output_filename):
    html_parts = []

    html_parts.append("<html><head><title>Heat Wave Animation Report</title></head><body>")

    html_parts.append(format_section_header("Python Code: Heat Wave Animation"))
    html_parts.append(parse_animation_code(code_filename))

    html_parts.append(format_section_header("Snapshots at Selected Times"))
    for plot_file in plot_filenames:
        html_parts.append(f'<img src="{plot_file}" alt="{plot_file}" width="500"><br>')

    html_parts.append(format_section_header("Animation"))
    html_parts.append(f'<img src="{gif_filename}" alt="Heat Wave Animation" width="600">')

    html_parts.append("</body></html>")

    report = '\n'.join(html_parts)
    write_html_report(report, output_filename)


# Run code
if __name__ == '__main__':
    code_file = '../array-computing/animate_heat_wave.py' # updated name
    plots = ['snapshot1.png', 'snapshot2.png', 'snapshot3.png']
    gif = 'heat_wave_animation.gif'  # whatever your GIF is named
    output_html = 'animation_report.html'

    create_html_report(code_file, plots, gif, output_html)
