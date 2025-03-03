
# Value of "n"
n = 5  # This is the value for maximum_integer

# Calculate the sum with for loop
sum_for_loop = 0
for i in range(1, n + 1):
    sum_for_loop += i

# Calculate the sum with formula
sum_formula = (n * (n + 1)) // 2

# Print out results
print(f"n = {n}")
print(f"sum(1, n) = {sum_for_loop}")
print(f"n(n+1)/2 = {sum_formula}")