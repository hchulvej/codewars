from gmpy2 import mpq, mpfr

def distances_from_average(test_list):
    avg = sum([mpq(n) for n in test_list]) / mpq(len(test_list))
    return [float(f"{(mpfr(avg) - n):.2f}") for n in test_list]

test_list = [55, 95, 62, 36, 48]

print(distances_from_average(test_list))