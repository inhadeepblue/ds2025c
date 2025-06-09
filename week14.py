def is_prime(n) -> bool:
  if n <= 1:
      return False
  else:
    for i in range(2, n):
        if n % i == 0:
          return False
  return True

s, e = map(int, input().split())
for i in range(s, e+1):
  if is_prime(i):
    print(i)