def get_positive_input(sPrompt):
    """Get positive numeric input with validation."""
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue < 0:
                print("Input must be a positive numeric value.")
            else:
                return fValue
        except ValueError:
            print("Input must be a positive numeric value.")

# Get user inputs with validation
fPrincipal = get_positive_input("What is the Original Deposit (positive value): ")
fAnnualInterestRate = get_positive_input("What is the Interest Rate (positive value): ")
nMonths = int(get_positive_input("What is the Number of Months (positive value): "))  
fGoal = get_positive_input("What is the Goal Amount (can enter 0 but not negative): ")

# Convert annual interest rate to decimal
fAnnualRateDecimal = fAnnualInterestRate / 100

# Calculate monthly interest rate (compounding)
fMonthlyRate = fAnnualRateDecimal / 12

# Initialize balance
fBalance = fPrincipal

# Loop to calculate monthly balance
for nMonth in range(1, nMonths + 1):
    fBalance += fBalance * fMonthlyRate
    print(f"Month: {nMonth} Account Balance is: $ {fBalance:,.2f}")

# Check if goal is reached within specified months
if fGoal > 0 and fBalance >= fGoal:
    print(f"You reached your goal of $ {fGoal:,.2f} after {nMonth} months.")
else:
    # Extend calculation if goal is not met within the initial months
    nAdditionalMonths = 0
    while fBalance < fGoal:
        fBalance += fBalance * fMonthlyRate
        nAdditionalMonths += 1

    nTotalMonths = nMonths + nAdditionalMonths
    print(f"It will take: {nTotalMonths} months to reach the goal of $ {fGoal:,.2f}")
