temperature_interval = 10
fahrenheit_temperature = 0
maximum_temperature = 100

print(f'T (°F)\t T (°C)')
print(15 * "=")

while fahrenheit_temperature <= maximum_temperature:
    celsius_temperature = 5/9 * (fahrenheit_temperature - 32)
    print(f'{fahrenheit_temperature:6}\t{celsius_temperature:6.3f}')
    fahrenheit_temperature += temperature_interval