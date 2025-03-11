def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
    """Convert Fahrenheit to Celsius using the formula."""
    return (fahrenheit_temperature - 32) * (5.0 / 9.0)

def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
    """Convert Celsius to Fahrenheit using the given formula."""
    return (9.0 / 5.0) * celsius_temperature + 32

if __name__ == '__main__':
    # Temperatures in Celsius
    test_temperatures_celsius = [0, 21, 100]  # Freezing, Room temp, Boiling

    # Print table header
    print(f"{'Celsius':^10} {'Fahrenheit':^12} {'Converted Back':^18}")
    print("=" * 40)

    # Convert and print result
    for celsius in test_temperatures_celsius:
        fahrenheit = convert_celsius_temperature_to_fahrenheit(celsius)
        converted_back = convert_fahrenheit_temperature_to_celsius(fahrenheit)
        print(f"{celsius:^10} {fahrenheit:^12.2f} {converted_back:^18.2f}")