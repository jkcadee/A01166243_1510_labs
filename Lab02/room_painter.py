COVERAGE = 400

length = int(input("Length of room in ft:"))

width = int(input("Width of room in ft:"))

height = int(input("Height of room in ft:"))

coats = int(input("Coats applied to room:"))

surface_area = (2 * length * width) + (2 * length * height) + (width * height)

coverage_needed = surface_area * coats

cans_of_paint_required = coverage_needed / COVERAGE

print("You must buy", cans_of_paint_required, "can(s) of paint.")
