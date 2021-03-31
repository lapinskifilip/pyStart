from math import *

# get x1, x2, y1, y2

x1 = int(input('Podaj punkt x1: '))
x2 = int(input('Podaj punkt x2: '))
y1 = int(input('Podaj punkt y1: '))
y2 = int(input('Podaj punkt y2: '))

# distance

dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# center

center_of_x = (x1 + x2) / 2
center_of_y = (y1 + y2) / 2

# radius
radius = dist / 2

# circle area
circle_area = pi * radius ** 2

# area

rectangle_a = abs(x2 - x1)
rectangle_b = abs(y2 - y1)

rectangle_area = rectangle_a * rectangle_b
rectangle_circ = (2 * rectangle_a) + (2 * rectangle_b)

print(f'Distance is: {dist}')
print(f'Center of X and Y is: {center_of_x} and {center_of_y}')
print(f'Radius is : {radius}')
print(f'Area of Circle is: {circle_area}')
print(f'Area nad Circuit of Rectangle is: {rectangle_area} and {rectangle_circ}')
