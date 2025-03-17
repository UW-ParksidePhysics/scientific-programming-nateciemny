def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if __name__ == '__main__':
    # Ask the user for a temperature
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius
    celsius = fahrenheit_to_celsius(fahrenheit)

    # Print results
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
