a = 21
b = 31
c = 324
d = 432
f = 232

max = a
min = a

if max <= b:max = b
if max <= c:max = c
if max <= d:max = d
if max <= f:max = f

if min >= b:max = b
if min >= c:max = c
if min >= d:max = d
if min >= f:max = f

print("Max = {0}, Min = {1}".format(max, min))