# Step 1: Define a function to get validated float input
def getFloatInput(strPrompt):
    while True:
        try:
            # Get input from the user and attempt to convert it to a float
            fltInput = float(input(strPrompt))
            
            # Check if the input is positive and non-zero
            if fltInput <= 0:
                print("Input must be a number greater than 0.")
                continue
            return fltInput
        except ValueError:
            # Handle non-numeric inputs
            print("Please enter a valid number.")

# Step 2: Define a function to calculate the median of a list
def getMedian(lstValues):
    lstValues.sort()
    
    # Check if the number of values is odd or even
    intLength = len(lstValues)
    if intLength % 2 == 1:
        return lstValues[intLength // 2]  # If odd, take the middle value
    else:
        # If even, take the average of the two middle values
        return (lstValues[intLength // 2 - 1] + lstValues[intLength // 2]) / 2

# Step 3: Main program function to handle property sales data
def main():
    lstPropertyValues = []  # List to store all the entered property values
    strContinue = "Y"  # Start with 'Y' to allow user input
    
    # Gather property sales values from the user
    while strContinue.lower() == "y":
        fltSalesPrice = getFloatInput("Enter property sales value: ")
        lstPropertyValues.append(fltSalesPrice)
        
        # Ask if the user wants to input another property value
        while True:
            strContinue = input("Enter another value Y or N: ").upper()
            if strContinue in ["Y", "N"]:
                break
            print("Please enter Y for Yes or N for No.")

    # Sort the list of property values from smallest to largest
    lstPropertyValues.sort()

    # Print each property value with currency formatting, aligning the $ symbol
    for i, fltValue in enumerate(lstPropertyValues, 1):
        print(f"Property {i:2}  $ {fltValue:,.2f}")

    # Calculate and print the minimum property value
    fltMin = min(lstPropertyValues)
    print(f"Minimum:     $ {fltMin:,.2f}")
    
    # Calculate and print the maximum property value
    fltMax = max(lstPropertyValues)
    print(f"Maximum:     $ {fltMax:,.2f}")
    
    # Calculate and print the total value of the properties
    fltTotal = sum(lstPropertyValues)
    print(f"Total:       $ {fltTotal:,.2f}")
    
    # Calculate and print the average property value
    fltAverage = fltTotal / len(lstPropertyValues)
    print(f"Average:     $ {fltAverage:,.2f}")
    
    # Calculate and print the median property value
    fltMedian = getMedian(lstPropertyValues)
    print(f"Median:      $ {fltMedian:,.2f}")
    
    # Calculate and print the commission
    fltCommission = fltTotal * 0.03
    print(f"Commission:  $ {fltCommission:,.2f}")

# Call the main function to run the program
main()
