import math

# Step 1: Get a positive float from user input
def getFloatInput(strPrompt):
    while True:
        try:
            fValue = float(input(strPrompt))
            if fValue > 0:
                return fValue
            else:
                print("Enter a positive number.")
        except ValueError:
            print("Invalid input. Try again.")

# Step 2: Calculate the number of gallons required (round up)
def getGallonsOfPaint(fSqft, fFeetPerGallon):
    return math.ceil(fSqft / fFeetPerGallon)

# Step 3: Calculate labor hours needed
def getLaborHours(fGallons, fLaborHoursPerGallon):
    return fGallons * fLaborHoursPerGallon

# Step 4: Calculate labor cost
def getLaborCost(fLaborHours, fLaborRate):
    return fLaborHours * fLaborRate

# Step 5: Calculate paint cost
def getPaintCost(fGallons, fPaintPrice):
    return fGallons * fPaintPrice

# Step 6: Get state-specific sales tax rate
def getSalesTax(strState):
    taxRates = {
        "CT": 0.06, "MA": 0.0625, "ME": 0.085, "NH": 0.0, "RI": 0.07, "VT": 0.06
    }
    return taxRates.get(strState.upper(), 0.0)

# Step 7: Display the cost estimate and save to a file
def showCostEstimate(fGallons, fLaborHours, fPaintCost, fLaborCost, fTax, fTotal, strLastName):
    print(f"Gallons of paint: {fGallons}")
    print(f"Hours of labor: {fLaborHours:.1f}")
    print(f"Paint charges: ${fPaintCost:.2f}")
    print(f"Labor charges: ${fLaborCost:,.2f}")
    print(f"Tax: ${fTax:.2f}")
    print(f"Total cost: ${fTotal:,.2f}")
    
    strFilename = f"{strLastName}_PaintJobOutput.txt"
    with open(strFilename, "w") as file:
        file.write(f"Gallons of paint: {fGallons}\n")
        file.write(f"Hours of labor: {fLaborHours:.1f}\n")
        file.write(f"Paint charges: ${fPaintCost:.2f}\n")
        file.write(f"Labor charges: ${fLaborCost:,.2f}\n")
        file.write(f"Tax: ${fTax:.2f}\n")
        file.write(f"Total cost: ${fTotal:,.2f}\n")
    print(f"File: {strFilename} was created.")

# Main function to execute the program
def main():
    # Step 1: Gather user input
    fSqft = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborRate = getFloatInput("Labor charge per hour: ")
    strState = input("State job is in: ")
    strLastName = input("Customer Last Name: ")

    # Step 2: Perform calculations
    fGallons = getGallonsOfPaint(fSqft, fFeetPerGallon)
    fLaborHours = getLaborHours(fGallons, fLaborHoursPerGallon)
    fPaintCost = getPaintCost(fGallons, fPaintPrice)
    fLaborCost = getLaborCost(fLaborHours, fLaborRate)
    fTaxRate = getSalesTax(strState)
    fTax = (fPaintCost + fLaborCost) * fTaxRate
    fTotal = fPaintCost + fLaborCost + fTax

    # Step 3: Display the results and save to a file
    showCostEstimate(fGallons, fLaborHours, fPaintCost, fLaborCost, fTax, fTotal, strLastName)

# Run the program
main()
