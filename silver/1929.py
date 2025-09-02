m, n = map(int, input().split())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n/2+1)):
        if n % i == 0:
            return False
    return True

for i in range(m, n+1):
    if is_prime(i):
        print(i)


# 에라토스테네스의 체 알고리즘
# 2부터 시작해서 소수의 배수를 지워나가는 알고리즘
# 지워지지 않고 남아 있는 수가 바로 소수이다.
def sieve(n):
    # n까지의 모든 수를 True로 표시 (소수 후보)
    prime = [True] * (n+1)
    prime[0], prime[1] = False, False  # 0과 1은 소수가 아님

    # 2부터 √n 까지 확인
    # n**0.5 -> ** 연산은 거듭제곱 
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:  # i가 아직 소수라면
            # i의 배수를 모두 False 처리

            # range(start, stop, step)
            for j in range(i*i, n+1, i):
                prime[j] = False

    # 소수만 뽑아내기
    return [i for i in range(2, n+1) if prime[i]]


# 사용 예시
m, n = map(int, input().split())
primes = sieve(n)  # n까지 소수 구하기
for p in primes:
    if p >= m:  # m 이상만 출력
        print(p)