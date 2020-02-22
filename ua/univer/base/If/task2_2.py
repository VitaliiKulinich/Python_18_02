a = 21
b = 31
c = 324
d = 432
max_ = a
if max_ <= b: max_ = b
if max_ <= c: max_ = c
if max_ <= d: max_ = d

counter = 0

if max_ == a:
    counter += 1
if max_ == b:
    counter += 1
if max_ == c:
    counter += 1
if max_ == b:
    counter += 1
print("Counter = {0}".format(counter))
