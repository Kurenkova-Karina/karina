#дз
#задание 1:  Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 1
b = "hello"
print(a)
print(b)

c = int(input("Введите число: "))
print(c)
d = input("Ваше имя: ")
print(d)

#задание 2: Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time_sec = int(input(Введите время в секундах: ))
time_sec = int(input("Введите время в секундах: "))
time_hour = int(time_sec)//60**2
time_min = int(time_sec)// 60 - int(time_hour)*60
time_sec2 = int(time_sec) - int(time_hour)*60**2 - int(time_min)*60

result = f"{time_hour} : {time_min} : {time_sec2}"
print(result)

#задание 3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
number = input("Введите число: ")
nn = number + number
nnn = number + number + number
number = int(number)
nn = int(nn)
nnn = int(nnn)
result = number + nn + nnn
print(result)

#задание 4: Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
#не знаю, как((

#5

earn = int(input("Ваша выручка: "))
costs = int(input("Ваши издержки: "))
if costs > earn:
    print ("Дела плохи")
elif costs == earn:
    print("Вы нашли баланс")
else:
    print("Вы в плюсе!")
profit = int(earn)// int(costs)
profit2 = f"Ваша рентабельность составляет {profit}"
print(profit2)
workers = int(input("Сколько у вас сотрудников: "))
profit_worker = int(profit)// int(workers)
profit_workers2 = f"Рентабельность на сотрудника {profit_worker}"
print(profit_workers2)

#6

a = float(input("В первый день вы пробежали: "))
b = float(input("Сколько нужно километров: "))
day = 1
while a <= b:
    a = a*1.1
    day +=1

    if a == b:
        print(day)
print(day)