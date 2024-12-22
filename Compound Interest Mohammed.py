# Get user input
principal = float(input("Enter the starting principal: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
times_compounded = int(input("How many times per year is the interest compounded? "))
years = float(input("For how many years will the account earn interest? "))

# Convert annual interest rate from percentage to decimal
r = annual_interest_rate / 100

# Calculate future value using the compound interest formula
future_value = principal * (1 + r / times_compounded) ** (times_compounded * years)

# Convert years to whole years and remaining months
whole_years = int(years)
remaining_months = int((years - whole_years) * 12)

# Output the result formatted to two decimal places
print(f"At the end of {whole_years} years and {remaining_months} months you will have $ {future_value:,.2f}")
