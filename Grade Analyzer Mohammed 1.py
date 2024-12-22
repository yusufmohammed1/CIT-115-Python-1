# Ask for Name
sName = input("Name of the person that we are calculating the grades for: ")

# Prompt for 4 test scores and validate
try:
    iTest1 = int(input("Test 1: "))
    iTest2 = int(input("Test 2: "))
    iTest3 = int(input("Test 3: "))
    iTest4 = int(input("Test 4: "))

    # Ensure scores are non-negative
    if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
        print("Test scores must be greater than 0.")
        exit()

except ValueError:
    print("Only whole numbers are accepted.")
    exit()
    
# Prompt for dropping the lowest grade
sDropLowest = input("Do you wish to Drop the Lowest Grade Y or N? ").upper()

# Validate Drop Lowest input
if sDropLowest not in ('Y', 'N'):
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

# Calculate the average based on Drop Lowest option
if sDropLowest == 'Y':
    # Find the lowest score and calculate average of the other 3
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        # iTest1 is the lowest
        fAverage = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        # iTest2 is the lowest
        fAverage = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        # iTest3 is the lowest
        fAverage = (iTest1 + iTest2 + iTest4) / 3
    else:
        # iTest4 is the lowest
        fAverage = (iTest1 + iTest2 + iTest3) / 3
elif sDropLowest == 'N':
    # Average all four scores if not dropping lowest
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4

# Determine the letter grade based on the average
if fAverage >= 97.0:
    sLetterGrade = "A+"
elif 94.0 <= fAverage < 96.9:
    sLetterGrade = "A"
elif 90.0 <= fAverage < 93.9:
    sLetterGrade = "A-"
elif 87.0 <= fAverage < 89.9:
    sLetterGrade = "B+"
elif 84.0 <= fAverage < 86.9:
    sLetterGrade = "B"
elif 80.0 <= fAverage < 83.9:
    sLetterGrade = "B-"
elif 77.0 <= fAverage < 79.9:
    sLetterGrade = "C+"
elif 74.0 <= fAverage < 76.9:
    sLetterGrade = "C"
elif 70.0 <= fAverage < 73.9:
    sLetterGrade = "C-"
elif 67.0 <= fAverage < 69.9:
    sLetterGrade = "D+"
elif 64.0 <= fAverage < 66.9:
    sLetterGrade = "D"
elif 60.0 <= fAverage < 63.9:
    sLetterGrade = "D-"
else:
    sLetterGrade = "F"

# Output the results formatted to 1 decimal place
print(f"{sName} test average is: {fAverage:.1f}")
print(f"Letter Grade for the test is: {sLetterGrade}")
