import random

answer = random.randint(1, 100)
win = False

for guesses in range(7):
    print(f"{7-guesses}번의 기회가 남았습니다. 숫자 입력 : ", end='')
    guess = int(input())

    if answer == guess:
        print("정답입니다!")
        win = True
        break
    elif answer > guess:
        print("입력하신 수는 정답보다 작은 수 입니다. LOW")
    else:
        print("입력하신 수는 정답보다 큰 수 입니다. HIGH")

if win:
    print("You win!")
else:
    print(f"You lose. The answer is {answer}.")
