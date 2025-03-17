import sys


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise IndexError(
                "Error: Missing Fahrenheit temperature. Usage: python script.py <temperature_in_fahrenheit>")

        # Convert the input to a float
        fahrenheit = float(sys.argv[1])
        celsius = fahrenheit_to_celsius(fahrenheit)

        # Print result
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

    except IndexError as e:
        print(e)
    except ValueError:
        print("Error: Please enter a valid number for the Fahrenheit temperature.")