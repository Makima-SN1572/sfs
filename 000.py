i = 0
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    print(i)

    i += 1

print("0-100之间的偶数累加结果是 %d" %result)