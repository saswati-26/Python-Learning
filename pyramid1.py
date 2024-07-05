row = int(input())
for i in range(1, row):
    for j in range(1, i + 1):
        print(i, end='')
    print()

# row = int(input())
# for i in range(1, row + 1):
#     print(str(i) * i)

# row = int(input())
# for i in range(1, row + 1):
#     print(((10 ** i - 1) // 9) * i)