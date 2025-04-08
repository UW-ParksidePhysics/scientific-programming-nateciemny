import matplotlib.pyplot as plt

def parse_sum_output(filename):
    tolerances = []
    errors = []
    maximum_indices = []

    with open(filename, 'r') as file:
        for line in file:
            if "epsilon:" in line and "exact error:" in line and "n=" in line:
                parts = line.strip().split(',')
                epsilon = float(parts[0].split(':')[1])
                error = float(parts[1].split(':')[1])
                n = int(parts[2].split('=')[1])
                tolerances.append(epsilon)
                errors.append(error)
                maximum_indices.append(n)

    return tolerances, errors, maximum_indices


def plot_logarithmic_sum_error(tolerances, errors, maximum_indices):
    plt.figure(figsize=(8, 5))

    plt.semilogy(maximum_indices, tolerances, 'o-', label='Tolerance (ε)')
    plt.semilogy(maximum_indices, errors, 's-', label='Exact Error')

    plt.xlabel('Maximum Index (n)')
    plt.ylabel('Log Scale Values')
    plt.title('Logarithmic Sum Error vs. Index')
    plt.grid(True, which="both", linestyle='--')
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    
    tolerances, errors, maximum_indices = parse_sum_output('logarithmic_sum.out')

    plot_logarithmic_sum_error(tolerances, errors, maximum_indices)
