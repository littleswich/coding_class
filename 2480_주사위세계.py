number = input().split(" ")
a, b, c = int(number[0]), int(number[1]), int(number[2])

# 모두 같은 경우
if a == b and b == c: print(10000 + a * 1000)

# 두 개만 같은 경우
elif a == b: print(1000 + a * 100)
elif b == c: print(1000 + b * 100)
elif a == c: print(1000 + a * 100)

# 모두 다른 경우
elif a != b and b != c and a != c: print(max(a, b, c) * 100)