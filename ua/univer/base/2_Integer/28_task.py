# день в році (від 1 до 365)
k = 9
# день тижня з якого почався рік (від 1 до 7)
n = 5
# день тижня знайдений остачою від ділення на 7 числа k (від 0 до 6)
x = k % 7
if x == 0: x = 7
# день тижня з врахуванням здвигу на початку року (від 0 до 6)
a = (x + n - 1) % 7
if a == 0: a = 7

print(x, a)