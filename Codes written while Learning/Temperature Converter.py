# Function Celsius
def Celsius(temperature):
  # Farenheit
  if unitTo == 'f' or unitTo == 'F':
    conversion = (temperature * 1.8) + 32
    print(f"{temperature:.2f} Celsius = {conversion:.2f} Farenheit")
  # Kelvin
  elif unitTo == 'k' or unitTo == 'K':
    conversion = temperature + 273.15
    print(f" {temperature:.2f} Celsius = {conversion:.2f} Kelvin")
  # Wrong Input
  else:
    print("Wrong Input")

# Function Farenheit
def Farenheit(temperature):
  # Kelvin
  if unitTo == 'k' or unitTo == 'K':
    conversion = (temperature - 32) * 0.55 + 273.15
    print(f"{temperature:.2f} Farenheit = {conversion:.2f} Kelvin")
  # Celsius
  elif unitTo == 'c' or unitTo == 'C':
    conversion = (temperature - 32) * 0.55
    print(f" {temperature:.2f} Farenheit = {conversion:.2f} Celsius")
  # Wrong Input
  else:
    print("Wrong Input")

# Function Kelvin
def Kelvin(temperature):
  # Farenheit
  if unitTo == 'f' or unitTo == 'F':
    conversion = (temperature - 273.15) * 1.8 + 32
    print(f"{temperature:.2f} Kelvin = {conversion:.2f} Farenheit")
  # Celsius
  elif unitTo == 'c' or unitTo == 'C':
    conversion = temperature - 273.15
    print(f" {temperature:.2f} Kelvin = {conversion:.2f} Celsius")
  # Wrong Input
  else:
    print("Wrong Input")

# To enter Loop
start = int(input("To start ENTER 1: "))

# Start of Loop
while start == 1:

  temperature = float(input("Enter the temperature: "))       # Accepting Temperature from user
  print("C for Celsius")
  print("K for Kelvin")
  print("F for Farenheit")
  unitFrom = input("Enter the unit of temperature: ")       # Enter unit of temperature

  # To convert from Celsius
  if unitFrom == 'c' or unitFrom == 'C':
    unitTo = input("Enter the unit you want to convert to: ")
    Celsius(temperature)    # Calling function Celsius

  # To convert from Kelvin
  elif unitFrom == 'k' or unitFrom == 'K':
    unitTo = input("Enter the unit you want to convert to: ")
    Kelvin(temperature)    # Calling function Kelvin

  # To convert from Farenheit
  elif unitFrom == 'f' or unitFrom == 'F':
    unitTo = input("Enter the unit you want to convert to: ")
    Farenheit(temperature)    # Calling function Farenheit
    
  # Wrong Input
  else:
    print("Wrong Input")

  start = int(input("To CONTINUE ENTER 1 or ENTER 0 to EXIT: "))    # To continue or stop
print("Thank you for using this program.")    # End of the program