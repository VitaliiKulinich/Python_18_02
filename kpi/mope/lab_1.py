import random

# set variables
column1, column2, column3, Y, by = [], [], [], [], []
a0, a1, a2, a3 = 1, 5, 43, 53
ay = 0

# generating arrays and finding Y
print("        Column 1  Column 2  Column 3")
for i in range(8):
    column1.append(round(random.random() * 20, 2))
    column2.append(round(random.random() * 20, 2))
    column3.append(round(random.random() * 20, 2))
    Y.append(round(a0 + a1 * column1[i] + a2 * column2[i] + a3 * column3[i], 2))
    ay += Y[i]
    print("Line {0}: {1:^8}  {2:^8}  {3:^8}  Y = {4:^8}".format(i + 1, column1[i], column2[i], column3[i], Y[i]))
ay = round(ay / 8, 2)

# finding Yet
X01 = (max(column1)+min(column1))/2
X02 = (max(column2)+min(column2))/2
X03 = (max(column3)+min(column3))/2
dX1 = X01-min(column1)
dX2 = X02-min(column2)
dX3 = X03-min(column3)
Xn1 = [round((column1[i] - X01)/dX1, 2) for i in range(8)]
Xn2 = [round((column2[i] - X02)/dX2, 2) for i in range(8)]
Xn3 = [round((column3[i] - X03)/dX3, 2) for i in range(8)]
Yet = round(a0 + a1*X01 + a2*X02 + a3*X03, 2)
print("\n    Xn1   |   Xn2    |   Xn3")
for i in range(8):
    print("{0:^10}|{1:^10}|{2:^10}".format(Xn1[i], Xn2[i], Xn3[i]))

# finding result
for i in range(8):
    if Y[i] > ay:
        by.append(Y[i])
result = min(by)

print("\nYet = {0}\nAverage of Y = {1}\nValue bigger than Y = {2}".format(Yet, ay, result))