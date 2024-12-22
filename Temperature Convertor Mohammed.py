#Welcome message
print("Welcome to Yusuf's Temperature Convertor!")

# Get the temperature value from the user
fTemp = float(input("Enter a temperature: "))

# Ask if the temperature is Fahrenheit or Celsius
sTemp_type = input("Is the temp F for Fahrenheit or C for Celsius? ").lower()

# Check if the input is valid
if sTemp_type == 'f':  # First condition: check if it's Fahrenheit
    if fTemp > 212:  # Nested condition for Fahrenheit
        print("Temp can not be > 212")
    else:  # If the temperature is valid
        fCelsius = (5.0 / 9) * (fTemp - 32)
        print(f"The Celsius equivalent is: {fCelsius:.1f}")

elif sTemp_type == 'c':  # Second condition: check if it's Celsius
    if fTemp > 100:  # Nested condition for Celsius
        print("Temp can not be > 100")
    else:  # If the temperature is valid
        fFahrenheit = ((9.0 / 5.0) * fTemp) + 32
        print(f"The Fahrenheit equivalent is: {fFahrenheit:.1f}")

else:  # If the input is neither 'f' nor 'c'
    print("You must enter a F or C")
