import random
secret_number = random.randint(1, 10)
attempts = 3
print("Гра 'Вгадай число'. Комп'ютер загадав число від 1 до 10. У вас є 3 спроби.")
for attempt in range(1, attempts + 1):
  guess = int(input(f"Спроба {attempt}. Введіть число: "))
  if guess == secret_number:
    print("Вітаю, ви вгадали!")
    break
  elif guess > secret_number:
    print("Менше")
  else:
    print("Більше")
else:
  print(f"Ви використали всі спроби. Було загадано число: {secret_number}")