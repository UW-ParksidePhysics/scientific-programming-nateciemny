#Date of Interest Rate Pull: 2/13/25

initial_amount_A = 1000
time_n = 3
interest_rate_P = 4.31
current_amount = initial_amount_A*(1 + (interest_rate_P / 100))**time_n

print("Initial Amount", initial_amount_A)
print("Interest Rate", interest_rate_P)
print("Current Amount", current_amount)