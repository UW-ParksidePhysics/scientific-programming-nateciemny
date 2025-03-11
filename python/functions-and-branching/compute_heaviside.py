def compute_heaviside(position):
    """Computes the Heaviside step function H(x)."""
    return 1 if position >= 0 else 0


def test_heaviside():
    """Tests the Heaviside function with given inputs and prints the results."""
    test_values = [-10, -10 - 15, 0, 10 - 15, 10]

    print(f"{'x':^10} {'H(x)':^10}")
    print("=" * 20)

    for x in test_values:
        print(f"{x:^10} {compute_heaviside(x):^10}")


if __name__ == '__main__':
    test_heaviside()
