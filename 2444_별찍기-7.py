a = int(input())
k = 1; num = "up"

for i in range(2 * a - 1):
    for v in range(a - k): print(" ", end = "")
    for j in range(a - (a - k)): print("*", end = "")
    for l in range(k - 1): print("*", end = "")
    if num == "up" and k < a: k += 1
    elif k == a: num = "down"

    if num == "down": k -= 1
    print()