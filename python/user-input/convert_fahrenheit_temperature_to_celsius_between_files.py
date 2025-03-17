def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def read_fahrenheit_values(filename):
    """Read Fahrenheit temperatures from a file, skipping the first three lines."""
    temperatures = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            if len(lines) < 4:
                print("Error: The file does not contain enough data.")
                return []

            for line in lines[3:]:
                if "Fahrenheit degrees:" in line:
                    words = line.split()
                    if len(words) >= 3:
                        try:
                            temp = float(words[2])  # Extract temperature
                            temperatures.append(temp)
                        except ValueError:
                            print(f"Warning: Could not process line: {line.strip()}")

        return temperatures

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []


def write_converted_temperatures(input_filename, output_filename):
    """Read Fahrenheit temperatures, convert to Celsius, and write results to a new file."""
    fahrenheit_values = read_fahrenheit_values(input_filename)

    if not fahrenheit_values:
        print("No valid temperatures found. Exiting.")
        return

    with open(output_filename, 'w') as file:
        file.write("Fahrenheit\tCelsius\n")  # Column headers
        file.write("----------------------\n")

        for f in fahrenheit_values:
            c = fahrenheit_to_celsius(f)
            file.write(f"{f:.1f}\t\t{c:.2f}\n")

    print(f"Converted temperatures have been written to '{output_filename}'.")


if __name__ == '__main__':
    input_file = "temperature.txt"
    output_file = "temperature_converted.txt"

    write_converted_temperatures(input_file, output_file)