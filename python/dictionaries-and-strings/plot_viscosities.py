import matplotlib.pyplot as plt
import numpy as np

# (a) Parse the viscosity data file
def parse_viscosity_data(filename):
    viscosity_data = {}
    with open(filename, 'r') as file:
        for line in file:
            if not line.strip() or line.strip().startswith('#'):
                continue

            parts = line.strip().split()

            try:
                # Extract last 3 elements as floats
                C = float(parts[-3])
                T0 = float(parts[-2])
                mu0 = float(parts[-1])
                # Everything before the last 3 parts is the name of gas
                name = ' '.join(parts[:-3]).lower()

                viscosity_data[name] = {
                    'viscosity': C,
                    'reference_temperature': T0,
                    'reference_viscosity': mu0
                }
            except ValueError as e:
                print(f"Skipping invalid line: {line.strip()} → {e}")

    return viscosity_data


# (b) Compute viscosity using Sutherland's formula
def calculate_viscosity(T, gas, viscosity_data):
    gas = gas.lower()
    if gas not in viscosity_data:
        raise ValueError(f"Gas '{gas}' not found in data.")

    data = viscosity_data[gas]
    C = data['viscosity']
    T0 = data['reference_temperature']
    mu0 = data['reference_viscosity']

    mu = mu0 * ((T0 + C) / (T + C)) * (T / T0) ** 1.5
    return mu


# (c) Plot viscosity vs. temperature for 3 gases
def plot_viscosity_curve(viscosity_data):
    T_vals = np.linspace(223, 373, 100)  # Temperature range [223K, 373K]
    gases = ['air', 'carbon dioxide', 'hydrogen']

    plt.figure(figsize=(8, 5))
    for gas in gases:
        mu_vals = [calculate_viscosity(T, gas, viscosity_data) for T in T_vals]
        plt.plot(T_vals, mu_vals, label=gas.title())

    plt.xlabel('Temperature (K)')
    plt.ylabel('Viscosity μ(T) (in 10⁻⁶ Pa·s)')
    plt.title('Viscosity of Gases vs. Temperature')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Main block
if __name__ == '__main__':
    data_file = 'viscosity_of_gases.dat'
    viscosity_data = parse_viscosity_data(data_file)
    plot_viscosity_curve(viscosity_data)

