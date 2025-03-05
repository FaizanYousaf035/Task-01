import math


# ----------------- LCM -----------------


def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

num1 = 10
num2 = 20

lcm = find_lcm(num1, num2)
print(f"LCM of {num1} and {num2} is {lcm}")




# ----------------- HCF -----------------
def find_hcf(x, y):
    return math.gcd(x, y)

num1 = 10
num2 = 20
hcf = find_hcf(num1, num2)

print(f" HCF of {num1} and {num2} is {hcf}")

# Output
# HCF of 10 and 20 is 10