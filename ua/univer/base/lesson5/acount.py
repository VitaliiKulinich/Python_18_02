def calculate_complex_rate(rate, money, period):
    month_sum = money
    for i in range(1, period+1):
        month_sum = round(month_sum + month_sum*(rate/100/12), 2)
        print(i, month_sum)
    return month_sum


def calculate_simple_rate(rate, money, period):
    for i in range(1, period + 1):
        result_sum = round(money + money * (rate / 100 / 12) * i, 2)
        print(i, result_sum)
    return result_sum