import math
shape = input("Enter the shape(triangle,square,rectangle,parallelogram,rhombus,circle,trapezium,cylinder,sphere,cone,cube) : ")
if shape == "triangle" :
   base = int(input("Enter the base(cm) : "))
   height = int(input("Enter the height(cm) : "))
   result = int(1/2 * base * height)
   print("triangle area is %s cm^2" %result)
elif shape == "square" :
   width = int(input("Enter the width(cm) : "))
   length = int(input("Enter the length(cm) : "))
   result = int(width * length)
   print("square area is %s cm^2" %result)
elif shape == "rectangle" :
   width = int(input("Enter the width(cm) : "))
   length = int(input("Enter the length(cm) : "))
   result = int(width * length)
   print("rectangle area is %s cm^2" %result)
elif shape == "circle" :
   radius = int(input("Enter the radius(cm) : "))
   result = int(math.pi * radius**2)
   print("circle area is %s cm^2" %result)
elif shape == "trapezium" :
   x = int(input("Enter the number : "))
   y = int(input("Enter the number : "))
   height = int(input("Enter the height(cm) : "))
   result = int(((x+y)*height)/2)
   print("trapezium area is %s cm^2" %result)
elif shape == "parallelogram" :
   width = int(input("Enter the width(cm) : "))
   length = int(input("Enter the length(cm) : "))
   result = int(width * length)
   print("parallelogram area is %s cm^2" %result)
elif shape == "rhombus" :
   width = int(input("Enter the width(cm) : "))
   length = int(input("Enter the length(cm) : "))
   result = int(width * length)
   print("rhombus area is %s cm^2" %result)
elif shape == "cylinder" :
   radius = int(input("Enter the radius(cm) : "))
   height = int(input("Enter the height(cm) : "))
   result = int(math.pi * radius**2 * height)
   print("cylinder volume is %s cm^3" %result)
elif shape == "sphere" :
   radius = int(input("Enter the radius(cm) : "))
   result = int(4/3 * math.pi * radius**3)
   print("sphere volume is %s cm^3" %result)
elif shape == "cone" :
   radius = int(input("Enter the radius(cm) : "))
   height = int(input("Enter the height(cm) : "))
   result = int(1/3 * math.pi * radius**2 * height)
   print("cone volume is %s cm^3" %result)
elif shape == "cube" :
   length = int(input("Enter the length(cm) : "))
   result = int(length**3)
   print("cube volume is %s cm^3" %result)