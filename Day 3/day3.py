# Day 3 of 30 Days of Python


# Declare your age as integer variable
age = 44

# Declare your height as a float variable
height = 6.3

# Declare a variable that store a complex number
comp_num = 1 + 1j


# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

tri_base = input("Triangle Base: ")
tri_height = input("Triangle Height: ")
tri_area = 0.5 * float(tri_base) * float(tri_height)


# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

tri_a = input("Side a: ")
tri_b = input("Side b: ")
tri_c = input("Side c: ")
tri_permimeter = tri_a + tri_b + tri_c

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rec_length = input("Rectangle Length: ")
rec_width = input("Rectangle Width: ")
rec_perimeter = 2 * (rec_length + rec_width)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.


cir_radius = input("Radius: ")
cir_area = 3.14 * float(cir_radius)**2
cir_circumference = 2.0 * 3.14 * float(cir_radius)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x1_8 = 0
y1_8 = 2 * x1_8 - 2
x2_8 = 1
y2_8 = 2 * x2_8 - 2

slope_8 = (y2_8 - y1_8) / (x2_8 - x1_8)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1_9, y1_9 = 2, 2 
x2_9, y2_9 = 6, 10
slope_9 = (y2_9 - y1_9) / (x2_9 - x1_9)

# Compare the slopes in tasks 8 and 9.
print("Slope 8 == Slope 9? ", slope_8 == slope_9)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_10 = [-10.0, -5.0, -1.0, 0.0, 1.0, 5.0, 10.0]
y = [float(x)**2 + 6.0 * float(x) + 9.0 for x in x_10]
print("y = x^2 + 6*x + 9: ", y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len('python') != len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print('jargon' in 'I hope this course is not full of jargon.')

# There is no 'on' in both dragon and python

print('on' in 'python' and 'on' in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string

print(str(float(len('python'))))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
even_num = int(input("Number: "))
result = (even_num % 2) == 0


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
comparison_number = int(2.7)
floor_division = 7 // 3
print(comparison_number == floor_division)

# Check if type of '10' is equal to type of 10


# Check if int('9.8') is equal to 10
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
