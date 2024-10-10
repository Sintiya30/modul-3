import math

# Function to find the roots of the quadratic equation
def find_roots(a, b, c):
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    print(f"Persamaan kuadrat: {a}x^2 + {b}x + {c}")
    print(f"Diskriminan: {discriminant}")
    
    # Check if discriminant is positive, zero or negative
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Merupakan akar berbeda")
        print(f"x1 = {root1}")
        print(f"x2 = {root2}")
    elif discriminant == 0:
        # One repeated real root
        root = -b / (2 * a)
        print("Merupakan akar kembar")
        print(f"akar = {root}")
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print("Merupakan akar kompleks")
        print(f"x1 = {real_part} + {imaginary_part}i")
        print(f"x2 = {real_part} - {imaginary_part}i")

# Input values for the quadratic equation
A = float(input("Nilai A: "))
B = float(input("Nilai B: "))
C = float(input("Nilai C: "))

# Call the function to calculate roots
find_roots(A, B, C)

