import random
def translate_feet(first_feet): # Функція перетворення bool в текст
    if first_feet == True:
        return "Користувач"
    else:
        return "Бот"
def flip_flop(first_feet): # Обмін ходу бота та користувача
    if first_feet == True:
        return False
    else:
        return True


def verification(number, c, first_feet, lower, higher): # Перевірка вгаданого числа з числом number.
    if number == c:
        print(f"Вітаю {translate_feet(first_feet)} переміг")
        return lower, higher
    elif number > c:
        print(f"Вам потрібно збільшити число")
        lower = c
        return lower, higher
    elif number < c:
        print(f"Вам потрібно зменшити число")
        higher = c
        return lower, higher




# — виклик і логіка

number = random.randint(1, 100) # Випад рандомного числа від 1 до 100.
print(f"{number} Число загадано.") # Повідомлення про задане число

first_feet = bool(random.randint(0, 1)) # Перевірка хто перший ходить. 0 - Бот. 1 - Користувач.
print(f"Першим ходить {translate_feet(first_feet)}")

higher = 100
lower = 1
while True:
    if first_feet == True:
        try:
            c = int(input("Введіть число: "))
        except ValueError:
            print("Це має бути ціле число")
        print(f"користувач {c}")
    
    else:
        c = random.randint(lower, higher)
        print(f"Бот {c}")
    
    
    lower, higher = verification(number, c, first_feet, lower, higher)    
    
    if number == c:
        break
    
    
    first_feet = flip_flop(first_feet)