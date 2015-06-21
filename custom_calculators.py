# Sample Python/Pygame Programs
# Calculate Miles Per Gallon
print("This program calculates Miles Per Gallon")

# Get miles driven from the user
miles_driven = input("Enter miles driven: ")
# Convert text entered to a floating point number
miles_driven = float(miles_driven)

# Get gallons used from the user
gallons_used = input("Enter gallons used: ")
# Convert text entered to a floating point number
gallons_used = float(gallons_used)

# Calculate and print the answer
mpg = miles_driven / gallons_used
print("Miles per gallon: ", mpg)

# Sample Python/Pygame Programs
# Calculate Kinectic Energy
print("This program calculates the kinectic energy of a moving object.")

m = float(input("Enter the object's mass in kilograms: "))
v = float(input("Enter the object's speed in meters per second: "))

e = 0.5 * m * v * v
print("The object has " + str(e) + " joules of energy.")

# Lab 1.2 Python/Pygame Programs
# Calculate Area of a Trapezoid
print("This program calculates the area of a trapezoid.")

h = float(input("Enter the height of the trapezoid: "))
l_top = float(input("Enter the lenght of the top base: "))
l_bottom = float(input("Enter the lenght of the bottom base: "))


A = 0.5 * (l_top + l_bottom) * h
print("The area is: ", A)


# Lab 1.1 Python/Pygame Programs
# Convert Temperature from Fahrenheit to Celcius
print("This program converts temperature from Fahrenheit to Celcius.")

# Get temperature in Fahrenheit from the user
temp_F = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celcius
temp_C = (temp_F - 32) * (5/9)

# Print the answer
print("The temperature in Celcius: ", temp_C)
