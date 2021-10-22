# Step 4 of Lab
# Formulas H through K
# These are written as functions

# Four Functions (Pythagorean Theorem, Discriminant, QuadPlus, QuadMinus)


# Formula H
def pythag(a, b):
	return (a**2 + b**2)**.5


# Formula I
def discriminant(a, b, c):
	return (b**2) - (4 * a * c)


# Formula J
def quadPlus(a, b, c):
	return (-b + (b**2 - (4 * a * c)**0.5)) / (2 * a)


# Formula K
def quadMinus(a, b, c):
	return (-b - (b**2 - (4 * a * c)**0.5)) / (2 * a)
