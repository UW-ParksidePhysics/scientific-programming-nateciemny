import sys

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if __name__ == '__main__':
    # Check that command-line argument was provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <temperature_in_fahrenheit>")
        sys.exit(1)

    # Read Fahrenheit temperature from the command line
    try:
        fahrenheit = float(sys.argv[1])
        celsius = fahrenheit_to_celsius(fahrenheit)

        # Print results
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    except ValueError:
        print("Please enter a valid number for the temperature in Fahrenheit.")
