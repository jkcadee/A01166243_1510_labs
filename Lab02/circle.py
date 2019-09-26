PI = 3.14159
radius = 0
radius = float(input("Enter radius:"))
circumference = 2 * PI * radius
area = PI * radius * radius
double_radius = radius * 2

double_circumference = 2 * PI * double_radius
double_area = PI * double_radius * double_radius

a_1 = double_area / area
c_1 = double_circumference / circumference

print(circumference)
print(area)
print("Area increases by ", a_1, " times when radius is doubled. Circumference increases by ", c_1, " times when radius is doubled.")

