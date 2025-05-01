def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def read_fahrenheit_from_file(filename):
    """Read Fahrenheit temperature from a file by skipping the first three lines and extracting the third word of the fourth line."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) < 4:
                print("Error: The file does not contain enough lines.")
                return None

            # Process line
            words = lines[3].split()  # Split the line
            if len(words) < 3:
                print("Error: The fourth line does not contain enough words.")
                return None

            return float(words[2])  # Convert the third word to float

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except ValueError:
        print("Error: Could not extract a valid temperature from the file.")
        return None

if __name__ == '__main__':
    filename = "temperature.txt"  # File containing the temperature data
    fahrenheit = read_fahrenheit_from_file(filename)

    if fahrenheit is not None:
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")