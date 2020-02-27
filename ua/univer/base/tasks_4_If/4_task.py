def count_positive_value(x1, x2, x3):
    #x1, x2, x3 = 16, 32, 213
    counter = 0
    if x1 > 0: counter += 1
    if x2 > 0: counter += 1
    if x3 > 0: counter += 1
    print("Positive count {0}".format(counter))

def count_negative_value(x1, x2, x3):
    counter = 0
    if x1 < 0: counter += 1
    if x2 < 0: counter += 1
    if x3 < 0: counter += 1
    print("Negative count {0}".format(counter))

