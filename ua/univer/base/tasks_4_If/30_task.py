x = 321

if x % 2:
    y = "Непарне"
else:
    y = "Парне"

if x // 100:
    z = "трьохзначне"
elif x // 10:
    z = "двозначне"
else:
    z = "однозначне"

print("{0} {1} число".format(y, z))
