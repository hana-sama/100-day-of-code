print("hi")
import mymodule


from my_parser import parse, convert
feet_inches = input("Enter feet and inches: ")

# 1 inch = 0.0254 1 feet = 0.3048
parsed = parse(feet_inches)
result = convert(parsed[0], parsed[1])
print(f"{parsed[0]} feet and {parsed[1]} inches is equal to {result:.2f} meters")
print(result)