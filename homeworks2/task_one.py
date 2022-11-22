from math import sqrt
point_a1 = int(input('Введите координату x(точки а):'))
point_a2 = int(input('Введите координату y(точки а):'))
point_b1 = int(input('Введите координату x(точки b):'))
point_b2 = int(input('Введите координату y(точки b):'))
distance_between_points = sqrt(pow(point_b2 - point_a2, 2) + pow(point_b1 - 
                                                                 point_a1, 2))
print(end='Расстояние между точками:')
print(distance_between_points)
