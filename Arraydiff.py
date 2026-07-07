def array_diff(a, b):
    for b_val in b:
        while b_val in a:
            a.remove(b_val)
                
    return a

print(array_diff([1,2,3], [1, 2]))