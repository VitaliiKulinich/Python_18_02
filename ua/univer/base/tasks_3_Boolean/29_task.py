x = 2
y = 3
x1 = 5
y1 = 6
x2 = 1
y2 = 2
xmax = max(x1, x2)
xmin = min(x1, x2)
ymax = max(y1, y2)
ymin = min(y1, y2)
if xmin <= x <= xmax and ymin <= y <= ymax:
    print("The point (X,Y) is inside the rectangle")
else:
    print("The point (X,Y) is outside the rectangle")