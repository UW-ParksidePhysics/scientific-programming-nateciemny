def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32

def test_conversion():
    """Verify that conversions return expected results within tolerance."""
    tolerance = 1e-2  # Small tolerance for floating-point precision
    test_passed = True

    # Celsius to Fahrenheit to Celsius
    c_temp = 100.0
    test_passed &= abs(celsius_to_fahrenheit(fahrenheit_to_celsius(c_temp)) - c_temp) < tolerance

    # Kelvin to Celsius to Kelvin
    k_temp = 273.15
    test_passed &= abs(kelvin_to_celsius(celsius_to_kelvin(k_temp)) - k_temp) < tolerance

    # Fahrenheit to Kelvin to Fahrenheit
    f_temp = 212.0
    test_passed &= abs(kelvin_to_fahrenheit(fahrenheit_to_kelvin(f_temp)) - f_temp) < tolerance

    assert test_passed, "Test failed! Check the conversion functions."
    print("All conversion tests passed successfully!")

    import sys

    def convert_from_command_line():
        """Converts user-provided temperature to the two other scales."""
        if len(sys.argv) < 3:
            print("Usage: python convert_temperature.py <temperature> <scale>")
            print("Example: python convert_temperature.py 21.3 C")
            sys.exit(1)

        try:
            temp = float(sys.argv[1])
            scale = sys.argv[2].upper()

            if scale == "C":
                f = celsius_to_fahrenheit(temp)
                k = celsius_to_kelvin(temp)
                print(f"{f:.1f} F {k:.1f} K")
            elif scale == "F":
                c = fahrenheit_to_celsius(temp)
                k = fahrenheit_to_kelvin(temp)
                print(f"{c:.1f} C {k:.1f} K")
            elif scale == "K":
                c = kelvin_to_celsius(temp)
                f = kelvin_to_fahrenheit(temp)
                print(f"{c:.1f} C {f:.1f} F")
            else:
                print("Invalid scale! Use C, F, or K.")

        except ValueError:
            print("Invalid temperature! Please enter a numeric value.")

    if __name__ == '__main__':
        if len(sys.argv) > 1 and sys.argv[1].lower() == "verify":
            test_conversion()