def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2+1)):
        if num % i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int,input().split()))
count = 0
for i in numbers:
    if is_prime(i):
        count += 1

print(count)