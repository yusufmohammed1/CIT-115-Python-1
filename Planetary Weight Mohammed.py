#1. Declare Named Constants:
MERCURY_FACTOR = 0.38
VENUS_FACTOR = 0.91
MOON_FACTOR = 0.165
MARS_FACTOR = 0.38
JUPITER_FACTOR = 2.34
SATURN_FACTOR = 0.93
URANUS_FACTOR = 0.92
NEPTUNE_FACTOR = 1.12
PLUTO_FACTOR = 0.066

#2. Ask Input:
sName = input ("What is your name: ")

fWeight = float(input("What is your weight: "))

print(f"{sName} here are your weights on our Solar System's planets:")

#3. Calculate the weights:
fMercuryWt = fWeight * MERCURY_FACTOR
fVenusWt   = fWeight * VENUS_FACTOR
fMoonWt    = fWeight * MOON_FACTOR
fMarsWt    = fWeight * MARS_FACTOR
fJupiterWt = fWeight * JUPITER_FACTOR
fSaturnWt  = fWeight * SATURN_FACTOR
fUranusWt  = fWeight * URANUS_FACTOR
fNeptuneWt = fWeight * NEPTUNE_FACTOR
fPlutoWt   = fWeight * PLUTO_FACTOR

#4. Output/Print:
print(f"Weight on Mercury: {fMercuryWt:10.2f} ")
print(f"Weight on Venus:   {fVenusWt:10.2f} ")
print(f"Weight on Moon:    {fMoonWt:10.2f}  ")
print(f"Weight on Mars:    {fMarsWt:10.2f}  ")
print(f"Weight on Jupiter: {fJupiterWt:10.2f} ")
print(f"Weight on Saturn:  {fSaturnWt:10.2f} ")
print(f"Weight on Uranus:  {fUranusWt:10.2f} ")
print(f"Weight on Neptune: {fNeptuneWt:10.2f} ")
print(f"Weight on Pluto:   {fPlutoWt:10.2f} ")
