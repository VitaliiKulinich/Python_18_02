#Variables
a = 7
b = 4
c = 2

#Quality of squares
q_a = a//c
q_b = b//c
q = q_a*q_b
print("Quality of squares = {0}".format(q))

#Square of free space
sq_a = a % c
sq_b = b % c
s = sq_a*b + sq_b*a - sq_a*sq_b
print("Square of free space = {0}".format(s))