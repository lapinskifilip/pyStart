# Area of Triangle

# |Ax * (By- Cy) + Bx * (Cy - Ay) + Cx* (Ay- By)|

from math import fabs

print('Witaj serdecznie drogi Uzytkowniku!')
print('Policzymy pole trojata, ale musisz mi podac jego wiercholki')

Ax = int(input("Podaj wiercholek Ax: "))
Ay = int(input("Podaj wiercholek Ay: "))
Bx = int(input("Podaj wiercholek Bx: "))
By = int(input("Podaj wiercholek By: "))
Cx = int(input("Podaj wiercholek Cx: "))
Cy = int(input("Podaj wiercholek Cy: "))

math = fabs(Ax * (By- Cy) + Bx * (Cy - Ay) + Cx* (Ay- By)) / 2

print(f'Pole tego trojkata to: {int(math)}')
