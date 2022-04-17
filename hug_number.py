n = int(input())
digits = list(input().split())
for i in range(0, n - 1):
    for j in range(0, n - 1 - i):
        if (digits[j+1] + digits[j]) > (digits[j] + digits[j+1]):
            digits[j], digits[j+1] = digits[j+1], digits[j]
print(*digits, sep='')
