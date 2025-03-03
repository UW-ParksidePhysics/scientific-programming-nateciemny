temperature_interval = 10
fahrenheit_temperature = 0
maximum_temperature = 100

print(f'T (°F)\t T (°C)\t T (°\u0108)')
print(30 * "=")

while fahrenheit_temperature <= maximum_temperature:
    celsius_temperature = 5/9 * (fahrenheit_temperature - 32)
    celsius_approximation = (fahrenheit_temperature - 30) / 2
    print(f'{fahrenheit_temperature:6}\t{celsius_temperature:6.3f}\t{celsius_approximation:6.3f}')
    fahrenheit_temperature += temperature_interval