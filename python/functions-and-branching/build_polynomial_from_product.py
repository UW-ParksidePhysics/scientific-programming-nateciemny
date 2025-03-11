def construct_polynomial_from_roots(roots):
    """Constructs a polynomial from given roots and returns its coefficients."""
    # Start with the polynomial being just [1] (which represents 1*x^0)
    coefficients = [1]

    for root in roots:
        # Multiply (x - root) with current polynomial
        new_coefficients = [0] * (len(coefficients) + 1)

        for i in range(len(coefficients)):
            new_coefficients[i] += coefficients[i]  # Copy coefficients
            new_coefficients[i + 1] -= coefficients[i] * root  # Multiply by -root

        coefficients = new_coefficients # Update term name

    return coefficients


if __name__ == '__main__':
    # Define test roots
    test_roots = [1, -2, 3]  # Example roots

    # Construct polynomial
    polynomial_coeffs = construct_polynomial_from_roots(test_roots)

    # Print result
    print(f"Polynomial coefficients for roots {test_roots}:")
    print(polynomial_coeffs)
