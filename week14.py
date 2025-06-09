n = int(input())  # N (명령어 개수)
stack = []  # 파이썬의 리스트를 이용

for i in range(n):
  order = input().strip()
  if 'push' in order:  # push X: 정수 X를 스택에 넣는 연산이다.
    number = order.split()  # ex) "push 1"  --> ["push", "1"]
    stack.append(number[-1])  # "1"
  elif order == 'pop':  # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(stack) == 0:  # 스택이 비어 있으면
      print(-1)
    else:
      print(stack.pop())  # 출력 및 삭제. Last In First Out
  elif order == 'size':  # size: 스택에 들어있는 정수의 개수를 출력한다.
    print(len(stack))
  elif order == 'empty':  # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    if len(stack) == 0:  # 스택이 비어 있으면
      print(1)
    else:
      print(0)
  elif order == 'top':  # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다. peek
    if len(stack) == 0:  # 스택이 비어 있으면
      print(-1)
    else:
      print(stack[-1])  # Top 값 출력