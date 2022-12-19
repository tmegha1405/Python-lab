area_square=lambda side:side*side
area_rectangle=lambda length,width:length*width
area_triangle=lambda breadth,height:(breadth*height)*0.5

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))

print( "Area of square is:",area_square(a))
print("Area of rectangle is:",area_rectangle(a,b))
print("Area of triangle is:",area_triangle(a,b))