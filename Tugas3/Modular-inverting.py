# a === b (mod m)
# a = k * m + b

# a = 3 * d
# b = 1, m = 13

# 3 * d = k * 13 + 1
# 3 * 9 = 2 * 13 + 1

a = 3
p = 13
print(pow(a,p-2) % p)