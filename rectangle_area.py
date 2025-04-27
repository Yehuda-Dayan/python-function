def area(length: float, width: float) -> float:
   shetach = length * width
   return shetach

parameters = float(input("Enter the length of the rectangle: ")), float(input("Enter the width of the rectangle: "))
area_of_rectangle = area(*parameters)
print(f"The area of the rectangle is: {area_of_rectangle}")