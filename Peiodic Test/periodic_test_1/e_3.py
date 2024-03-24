a = int(input("Enter a number:-"))
b = int(input("Enter a number:-"))
c = int(input("Enter a number:-"))

if a*a == b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a:
    print("Pythagorean triplets")
else:
    print("Not a Pythagorean triplets")