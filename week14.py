import math

def is_prime(n) -> bool:
  if n <= 1:
      return False
  elif n == 2:
      return True
  elif n % 2 == 0:
      return False
  else:
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
          return False
  return True

s, e = map(int, input().split())
for i in range(s, e+1):
  if is_prime(i):
    print(i)