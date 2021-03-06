# https://www.mathsisfun.com/algebra/polynomials.html
# each element of the list represents the corresponding coefficient of x. 
# list [1, 2, 3, 4] represents the polynomial `1x^0 + 2x^2 + 3x^3 + 4x^4

def print_polynomial_bad(coefs):
    for i in range(0, len(coefs)):
        print(str(coefs[i]) + "x^" + str(i), end = "")
        if i != len(coefs) - 1:
            print(" + ", end = "")
    print("")

# Use this version
def print_polynomial(coefs):
    strs = []
    for i in range(0, len(coefs)):
        if coefs[i] != 0:
            strs.append(str(coefs[i]) + "x^" + str(i))
    print(" + ".join(strs))

# Tests
print_polynomial_bad([])
print_polynomial_bad([1])
print_polynomial_bad([1, 2, 3])
print_polynomial_bad([1, 2, 0, 3])

print_polynomial([])
print_polynomial([1])
print_polynomial([1, 2, 3])
print_polynomial([1, 2, 0, 3])