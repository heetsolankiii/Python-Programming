start = int(input("To start ENTER 1: "))    # Start

# Start of Loop
while start == 1:

  temperature = float(input("Enter the temperature: "))       # Enter Temperature
  print("C for Celsius")
  print("K for Kelvin")
  print("F for Farenheit")
  unitFrom = input("Enter the unit of temperature: ")       # Enter unit of temperature

# To convert from Celsius
  if unitFrom == 'c' or unitFrom == 'C':
    unitTo = input("Enter the unit you want to convert to: ")
    if unitTo == 'f' or unitTo == 'F':      # Farenheit
      conversion = (temperature * 1.8) + 32
      print(f"{temperature:.2f} Celsius = {conversion:.2f} Farenheit")
    elif unitTo == 'k' or unitTo == 'K':        # Kelvin
      conversion = temperature + 273.15
      print(f" {temperature:.2f} Celsius = {conversion:.2f} Kelvin")
    else:       # Wrong Input
      print("Wrong Input")

# To convert from Kelvin
  elif unitFrom == 'k' or unitFrom == 'K':
    unitTo = input("Enter the unit you want to convert to: ")
    if unitTo == 'f' or unitTo == 'F':      # Farenheit
      conversion = (temperature - 273.15) * 1.8 + 32
      print(f"{temperature:.2f} Kelvin = {conversion:.2f} Farenheit")
    elif unitTo == 'c' or unitTo == 'C':        # Celsius
      conversion = temperature - 273.15
      print(f" {temperature:.2f} Kelvin = {conversion:.2f} Celsius")
    else:       # Wrong Input
      print("Wrong Input")

# To convert from Farenheit
  elif unitFrom == 'f' or unitFrom == 'F':
    unitTo = input("Enter the unit you want to convert to: ")
    if unitTo == 'k' or unitTo == 'K':      # Kelvin
      conversion = (temperature - 32) * 0.55 + 273.15
      print(f"{temperature:.2f} Farenheit = {conversion:.2f} Kelvin")
    elif unitTo == 'c' or unitTo == 'C':        # Celsius
      conversion = (temperature - 32) * 0.55
      print(f" {temperature:.2f} Farenheit = {conversion:.2f} Celsius")
    else:       # Wrong Input
      print("Wrong Input")

  else:     # Wrong Input
    print("Wrong Input")

  start = int(input("To CONTINUE ENTER 1 or ENTER 0 to EXIT: "))
print("Thank you for using this program")