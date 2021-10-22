def f_to_c(temp1):
	return (temp1 - 32) * 5 / 9


def c_to_f(temp2):
	return (temp2 * 9 / 5) + 32


temp1 = int(input("Enter a number in F to convert to C: "))
temp2 = int(input("Enter a number in C to convert to F: "))

print(str(temp1) + " degrees F is " + str(f_to_c(temp1)) + " degrees C")
print(str(temp2) + " degrees C is " + str(c_to_f(temp2)) + " degrees F")
